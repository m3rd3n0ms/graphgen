from django.shortcuts import render
from .models import *
import pandas as pd

# Formateamos columnas tipo float con coma decimal y dos decimales
pd.options.display.float_format = '{:,.2f}'.format

# Create your views here.

def home(request):

    # Recuperamos nombres de departamentos
    df_departments = pd.DataFrame(Department.objects.all().values())

    # Validamos que existan registros
    error_message = None
    if df_departments.shape[0] > 0:

        # obtenemos todas las transacciones de ventas 
        df_sales = pd.DataFrame(Transaction.objects.all().values().filter(tr_type_doc = 'S')) 

        # Igualamos columnas y unimos Ventas con Departamentos
        df_sales['de_code'] = df_sales['tr_department_id']
        trde_merge = pd.merge(df_departments, df_sales, on = 'de_code').drop(['de_enterprise_id', 'de_store_id'], axis=1)

        # Obtenemos dataframe de Ventas agrupado por departamentos
        sales_group = trde_merge.groupby('de_name').sum(numeric_only=True)

        # Obtenemos todas las transacciones de Compras
        df_purchases = pd.DataFrame(Transaction.objects.all().values().filter(tr_type_doc = 'P')) 

        # Igualamos columnas y unimos Compras con Departamentos
        df_purchases['de_code'] = df_purchases['tr_department_id']
        trde_merge2 = pd.merge(df_departments, df_purchases, on = 'de_code').drop(['de_enterprise_id', 'de_store_id'], axis=1)

        # Obtenemos dataframe de Compras agrupado por departamentos
        df_purchase_group = trde_merge2.groupby('de_name').sum(numeric_only=True).reset_index()

        # Obtenemos dataframe de Ventas y Compras por Departamento
        df_sales_purchases = pd.merge(sales_group, df_purchase_group, on = 'de_name').drop(['tr_code_x', 'tr_code_y'], axis=1).rename({'de_name': 'Department', 'tr_usd_value_x': 'Sales', 'tr_usd_value_y': 'Purchases'},axis=1)

        # Obtenemos margen de ganancia (Ventas - Compras)
        df_sales_purchases['Profit'] = df_sales_purchases['Sales'] - df_sales_purchases['Purchases']

        # Obtenemos totales de Ventas, Compras y Profit
        total_ventas = df_sales_purchases['Sales'].sum(numeric_only=True)
        total_ventas = (f'{total_ventas:,.2f}')
        total_compras = df_sales_purchases['Purchases'].sum(numeric_only=True)
        total_compras = '{:,.2f}'.format(total_compras)
        total_profit = df_sales_purchases['Profit'].sum(numeric_only=True)
        total_profit = '{:,.2f}'.format(total_profit)

        # Obtenemos datos para graficas
        list_department = df_sales_purchases['Department'].tolist()
        list_sale = df_sales_purchases['Sales'].tolist()
        list_purchase = df_sales_purchases['Purchases'].tolist()

        # Agregamos fila de totales al dataframe
        df_sales_purchases = df_sales_purchases.append({'Department': 'Totals', 'Sales': total_ventas, 'Purchases': total_compras, 'Profit': total_profit}, ignore_index=True)

    else:
        error_message = 'No records in database'

    # Generamos contexto para la plantilla
    context = {
        "error_message" : error_message,
        "labels": list_department,
        "data_sale": list_sale,
        "data_purchase": list_purchase,
        "transaction": df_sales_purchases.to_html(),
    }

    # Devolvemos renderizado de dataframe de Ventas y Compras 
    return render(request,"graph01/graph01.html", context)
