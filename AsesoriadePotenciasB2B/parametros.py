# Librerías
import pandas as pd 
from datetime import date, datetime

# Parámetros
# Precio exceso de Potencia 
tbl_excPot_med123 = pd.read_excel(r'C:\Users\Usuario\Documents\TFG\AsesoriadePotenciasB2B\exceles\all_tables_need.xlsx', sheet_name='termino_excPotencia_med123', index_col=0, engine='xlrd')
tbl_excPot_med4y5 = pd.read_excel(r'C:\Users\Usuario\Documents\TFG\AsesoriadePotenciasB2B\exceles\all_tables_need.xlsx', sheet_name='termino_excPotencia_med4y5', index_col=0, engine='xlrd')

# Coeficiente Kp
tbl_coeficiente_Kp = pd.read_excel(r'C:\Users\Usuario\Documents\TFG\AsesoriadePotenciasB2B\exceles\all_tables_need.xlsx', sheet_name='coeficiente_Kp', index_col=0, engine='xlrd')

# Precio termino de potencia
tbl_termPrecPot = pd.read_excel(r'C:\Users\Usuario\Documents\TFG\AsesoriadePotenciasB2B\exceles\all_tables_need.xlsx', sheet_name='termino_precio_potencia', index_col=0, engine='xlrd')

# Precio terminon de potencia
tarifas = ['2_0TD', '3_0TD', '6_1TD', '6_2TD', '6_3TD', '6_4TD'] 
#ó tarifas ={tarifa : ['2_0TD', '3_0TD', '6_1TD', '6_2TD', '6_3TD', '6_4TD']}

# Tipo Suministro
tipo_punto = [1, 2, 3, 4, 5] #ó tipo_punto ={punto_medida : [1, 2, 3, 4, 5]}

#Periodos 
periodos = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6']

# Festivos nacionales
festivos_nacionales = ['01/01/2019', '19/04/2019', '01/05/2019', '15/08/2019',
'12/10/2019','01/11/2019','06/12/2019','25/12/2019','01/01/2020','06/01/2020','10/04/2020','01/01/2020','01/05/2020',
'15/08/2020','12/10/2020','08/12/2020','25/12/2020','01/01/2021','06/01/2021','02/04/2021','01/05/2021','12/10/2021',
'01/11/2021','06/12/2021','08/12/2021','25/12/2021','01/01/2022','06/01/2022','15/04/2022','15/08/2022','12/10/2022',
'01/11/2022','06/12/2022','08/12/2022']
#list comprehension
my_date_list = [datetime.strptime(x,'%d/%m/%Y') for x in festivos_nacionales]

# Tabla reparto potencias tramos
tabla_periodos = pd.read_excel("exceles/GeneradorCurva.xlsm", sheet_name = ('Horario'), usecols = 'F:CX', nrows = 12)
tabla_periodos.columns = ['Mes', '00:15:00', '00:30:00', '00:45:00', '01:00:00', '01:15:00', '01:30:00',
       '01:45:00', '02:00:00', '02:15:00', '02:30:00', '02:45:00', '03:00:00',
       '03:15:00', '03:30:00', '03:45:00', '04:00:00', '04:15:00', '04:30:00',
       '04:45:00', '05:00:00', '05:15:00', '05:30:00', '05:45:00', '06:00:00',
       '06:15:00', '06:30:00', '06:45:00', '07:00:00', '07:15:00', '07:30:00',
       '07:45:00', '08:00:00', '08:15:00', '08:30:00', '08:45:00', '09:00:00',
       '09:15:00', '09:30:00', '09:45:00', '10:00:00', '10:15:00', '10:30:00',
       '10:45:00', '11:00:00', '11:15:00', '11:30:00', '11:45:00', '12:00:00',
       '12:15:00', '12:30:00', '12:45:00', '13:00:00', '13:15:00', '13:30:00',
       '13:45:00', '14:00:00', '14:15:00', '14:30:00', '14:45:00', '15:00:00',
       '15:15:00', '15:30:00', '15:45:00', '16:00:00', '16:15:00', '16:30:00',
       '16:45:00', '17:00:00', '17:15:00', '17:30:00', '17:45:00', '18:00:00',
       '18:15:00', '18:30:00', '18:45:00', '19:00:00', '19:15:00', '19:30:00',
       '19:45:00', '20:00:00', '20:15:00', '20:30:00', '20:45:00', '21:00:00',
       '21:15:00', '21:30:00', '21:45:00', '22:00:00', '22:15:00', '22:30:00',
       '22:45:00', '23:00:00', '23:15:00', '23:30:00', '23:45:00', '00:00:00']

