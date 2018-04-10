import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import csv






with open('train.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    Imps=0.0
    Total_clicks = 0
    price=0.0
    click_price=0.0
    Weekday_Imps=[0,0,0,0,0,0,0]
    Weekday_clicks=[0,0,0,0,0,0,0]
    Weekday_ctr=[0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    Weekday_price=[0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    Hour_clicks=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0, 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    Hour_Imps= [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0, 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    ie_imps=0.0
    ie_clicks=0.0
    chrome_imps=0.0
    chrome_clicks=0.0
    imps_3427=0.0
    clicks_3427=0.0
    imps_1458=0.0
    click_1458=0.0

    for line in csv_reader:
        Imps = Imps + 1
        price=price+ + float(line[21])
        Weekday_Imps[int(line[1])] = Weekday_Imps[int(line[1])]+1
        Weekday_price[int(line[1])]= Weekday_price[int(line[1])]+float(line[21])
        Hour_Imps[int(line[2])]=Hour_Imps[int(line[2])] +1

        if line[5] == "windows_ie":
            ie_imps= ie_imps + 1

        if line[5] == "windows_chrome":
            chrome_imps= chrome_imps + 1

        if line[23] == "3427":
            imps_3427= imps_3427 + 1.0

        if line[23] == "1458":
            imps_1458= imps_1458 + 1.0



        if line[0] == "1":
            Total_clicks = Total_clicks+1
            click_price = click_price+ float(line[21])

            Weekday_clicks[int(line[1])] = Weekday_clicks[int(line[1])]+1
            Hour_clicks[int(line[2])]=Hour_clicks[int(line[2])] +1
            #Weekday_clicks[0]= (Weekday_clicks[0]) +1
            if line[5] == "windows_ie":
                ie_clicks= ie_clicks + 1

            if line[5] == "windows_chrome":
                chrome_clicks= chrome_clicks + 1

            if line[23] == "3427":
                clicks_3427= clicks_3427 + 1

            if line[23] == "1458":
                click_1458= click_1458 + 1


    A_ctr=Total_clicks/Imps
    #for x in Weekday_ctr:
     #   Weekday_ctr[x]= Weekday_clicks[x] / Weekday_Imps[x]

    Weekday_ctr=[(x*1.0)/y for x, y in zip(Weekday_clicks, Weekday_Imps)]
    Weekday_cpm=[(x*1.0)/y for x, y in zip(Weekday_price, Weekday_Imps)]
    Hours_ctr=[(x*1.0)/y for x, y in zip(Hour_clicks, Hour_Imps)]
    ie_ctr= ie_clicks/ie_imps
    chrome_ctr= chrome_clicks/chrome_imps
    ctr_3427=clicks_3427/imps_3427
    ctr_1458=click_1458/imps_1458

    plot_i=[ie_ctr,chrome_ctr]
    plot_a=[ctr_3427,ctr_1458]

    print('Number of impressions ' + repr(Imps))
    print('Number of total clicks '+repr(Total_clicks))
    print('AVG CTR '+ repr(A_ctr))
    print('AVG CPC '+ repr(click_price/Total_clicks))
    print('AVG CPM '+ repr(price/Imps))
    print('Weekday clicks '+ repr(Weekday_clicks))
    print('Weekday CTR '+ repr(Weekday_ctr))
    print('Weekday CPM '+ repr(Weekday_cpm))
    print('Hours CTR '+ repr(Hours_ctr))
    print('Internet explorer CTR '+ repr(ie_ctr))
    print('Chrome CTR '+ repr(chrome_ctr))
    print('CTR for advertiser 3427  ' +repr(ctr_3427))
    print('CTR for advertiser 1458  '+repr(ctr_1458))

    #plt.bar([0, 1], [ctr_3427, ctr_1458])
    #plt.show()#plt.hist(x= (ie_ctr,chrome_ctr), label=["ie", "chrome"])
    #plt.hist(ie_ctr, bins=50, color='b', label='Internet Explorer')
    #plt.hist(chrome_ctr, bins=50, color='r', label='Chrome')
    #plt.xlabel('Browser')
    #plt.title('CTR by Browser')
    #plt.ylabel('CTR')
    #plt.show()
    

