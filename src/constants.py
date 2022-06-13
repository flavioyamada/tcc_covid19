IBGE_FTP_BASE_URL = 'https://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/{}'

NUMBER_FILE = 7

SOURCE_URLS = {
    "conjunto1.zip": IBGE_FTP_BASE_URL.format('Aglomerados_subnormais/Aglomerados_subnormais_informacoes_territoriais/tabelas_xls/UFs_Municipios.zip'),
    "conjunto2.zip": IBGE_FTP_BASE_URL.format('Entorno_dos_Domicilios/xls/Municipios/sao_paulo.zip'),
    "conjunto3.zip": IBGE_FTP_BASE_URL.format('Resultados_do_Universo/xls/Municipios/sao_paulo_20190207.zip'),
    "conjunto4.zip": IBGE_FTP_BASE_URL.format('Educacao_e_Deslocamento/xls/sao_paulo_xls.zip'),
    "conjunto5.zip": IBGE_FTP_BASE_URL.format('Trabalho_e_Rendimento/xls/sao_paulo_munic_xls.zip'),
    "conjunto6.zip": IBGE_FTP_BASE_URL.format('Familias_e_Domicilios/xls/Unidades_da_Federacao/sao_paulo_xls.zip'),
    "conjunto7.zip": "https://raw.githubusercontent.com/seade-R/dados-covid-sp/master/data/plano_sp_leitos_internacoes_serie_nova_variacao_semanal.csv.zip"
}
