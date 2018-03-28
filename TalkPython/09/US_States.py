#!python3

#https://github.com/talkpython/100daysofcode-with-python-course/tree/master/days/07-09-data-structures

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

states_list = [
    'Oklahoma',
    'Kansas',
    'North Carolina',
    'Georgia',
    'Oregon',
    'Mississippi',
    'Minnesota',
    'Colorado',
    'Alabama',
    'Massachusetts',
    'Arizona',
    'Connecticut',
    'Montana',
    'West Virginia',
    'Nebraska',
    'New York',
    'Nevada',
    'Idaho',
    'New Jersey',
    'Missouri',
    'South Carolina',
    'Pennsylvania',
    'Rhode Island',
    'New Mexico',
    'Alaska',
    'New Hampshire',
    'Tennessee',
    'Washington',
    'Indiana',
    'Hawaii',
    'Kentucky',
    'Virginia',
    'Ohio',
    'Wisconsin',
    'Maryland',
    'Florida',
    'Utah',
    'Maine',
    'California',
    'Vermont',
    'Arkansas',
    'Wyoming',
    'Louisiana',
    'North Dakota',
    'South Dakota',
    'Texas',
    'Illinois',
    'Iowa',
    'Michigan',
    'Delaware'
]

def print_the_10_of_each():
    print('#### Print index 10 of each ####')
    print(next(x for i,x in enumerate(us_state_abbrev) if i == 9))
    print(states_list[9])

def print_the_45_key_in_dictionary():
    print('#### Print the 45 key of dictionary ####')
    print(next(x for i,x in enumerate(us_state_abbrev) if i == 44))

def print_the_27_value_in_dictionary():
    print('#### Print the 27 value of dictionary ####')
    print(us_state_abbrev[next(x for i,x in enumerate(us_state_abbrev) if i == 26)])

def replace_the_15_key_in_dictionary_from_28_item_in_list():
    # wtf?
    print('#### Replace the 15 key in dictionary from 28 item in list ####')
    state = next(x for i,x in enumerate(us_state_abbrev) if i == 14)
    abv = us_state_abbrev[state]
    del us_state_abbrev[state]
    us_state_abbrev[states_list[27]] = abv

def main():
    print_the_10_of_each()
    print_the_45_key_in_dictionary()
    print_the_27_value_in_dictionary()
    replace_the_15_key_in_dictionary_from_28_item_in_list()


if __name__ == '__main__':
    main()
