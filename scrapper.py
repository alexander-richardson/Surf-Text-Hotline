from requests import get
from bs4 import BeautifulSoup
from spots import spotsdict
from darksky import weather_forcast


def get_soup(location):
    input = str(spotsdict.get(location))
    response = get('https://magicseaweed.com/Smugglers-Cove-Surf-Report/{}/'.format(input))
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup 




def get_report(location):
    soup = get_soup(location)
        ####################Scrapped Info#############
    # #list of all items as bs4.eleme'n't.ResultSet
    height = soup.find(class_='rating-text text-dark')


    ###wave height as an int
    str_height = str(height)
    min_height = int(str_height[38])
    max_height = int(str_height[40])

    # Find current wave height as a string
    height_str = soup.find("li", attrs={'class':'rating-text text-dark'}).text
    #current wind conditions
    wind= soup.find("p", attrs={'class':'h5 nomargin-top'}).text
    #Primary swell
    primary_swell = soup.find("div", attrs={'class':'inline-block'}).text
    #TODO trying a few things but still only getting primary swell information when wanting second 
    secondary_swell = soup.find("div", attrs={'inline-block':'strong'})


    #Find all text in surf report tide table
    tide_table = interval = soup.find("table", attrs={'class':'table table-sm table-striped table-inverse table-tide'}).text
    first_high_tide = tide_table[8:15]
    second_high_tide = tide_table[52:58]

    first_low_tide = tide_table[28:35]
    second_low_tide = tide_table[72:80]
    
    weather = soup.find_all(class_='list-group-item')
    weather1 = weather

    #not sure what I was doing here but looks like this was the same info as the tide table but formated differentl?
    right_coloumn = soup.find_all(class_= 'text-right')
    sunrise = right_coloumn[6].text

    #Sample output(TODO secondary swell intervals)
    report = "Right now the waves are between " + str(min_height) + " and " + str(max_height) + "ft with a " + wind + " wind. Primary swell is " + primary_swell + ' ' + weather_forcast

    return(report)



