def corr_offense_borough (data, offense):
    '''Get correlation coefficient per borough for one offense_category.'''
    data_filter = data[data['offense_category'] == offense]
    #Bronx
    data_brx = data_filter[data_filter['borough'] == 'Bronx']
    corr_brx = data_brx['unemprate'].corr(data_brx['count'])
    print("Correlation coefficient between", offense, "offenses in Bronx and Unemployment Rate:", corr_brx)

    #Brooklyn
    data_brl = data_filter[data_filter['borough'] == 'Brooklyn']
    corr_brl = data_brl['unemprate'].corr(data_brl['count'])
    print("Correlation coefficient between", offense, "offenses in Brooklyn and Unemployment Rate:", corr_brl)

    #Manhattan
    data_man = data_filter[data_filter['borough'] == 'Manhattan']
    corr_man = data_man['unemprate'].corr(data_man['count'])
    print("Correlation coefficient between", offense, "offenses in Manhattan and Unemployment Rate:", corr_man)

    #Queens
    data_que = data_filter[data_filter['borough'] == 'Queens']
    corr_que = data_que['unemprate'].corr(data_que['count'])
    print("Correlation coefficient between", offense, "offenses in Queens and Unemployment Rate:", corr_que)

    #Staten Island
    data_isl = data_filter[data_filter['borough'] == 'Staten Island']
    corr_isl = data_isl['unemprate'].corr(data_isl['count'])
    print("Correlation coefficient between", offense, "offenses in Staten Island and Unemployment Rate:", corr_isl)
