# Final Version:
# Get user report option
m = input('Enter Report Short Code: (E.g: m: Madhavi) ')
if m == 'm':
    MADHAVI_URL = 'https://soas.hubbub.net/p/debate310121/supporters/'
    pages = requests.get(MADHAVI_URL)
    DIR_PREFIX = 'User/Madhavi/'
else:
    URL = 'https://soas.hubbub.net/p/TamilStudies/supporters/'
    pages = requests.get(URL)
    DIR_PREFIX = ''

soup = BeautifulSoup(pages.content, 'html.parser')

with open(DIR_PREFIX + 'donations.txt', 'r', encoding="utf-8") as f:
    data = f.readlines()
    with open(DIR_PREFIX + 'donations_' + datetime.today().strftime('%Y_%b_%d__%Hh_%Mm_%Ss') + '.txt', 'w', encoding="utf-8") as out:
        out.writelines(data)

f = open(DIR_PREFIX + 'donations.txt', 'w', encoding="utf-8")
fn = open(DIR_PREFIX + 'new donations.txt', 'w', encoding='utf-8')

# Get the raised amount
f.write('=========================================================\n')
f.write('Date of the report: ' + datetime.today().strftime('%d-%b-%Y, Time: %Hh:%Mm:%Ss') + '\n')
x = soup.find_all(class_='project-amount-raised')[0].get_text().strip()
f.write('Amount Raised: ' + x + '\n')

# Get the target amount
x = soup.find_all(class_='project-total-amount')[0].get_text().strip()
f.write('Target: ' + x + '\n')

# project-stat-amount
x = soup.find_all(class_='project-stat-amount')[0].get_text().strip()
f.write('Percentage Funded: ' + x + '\n')

# project-stat-amount
x = soup.find_all(class_='project-stat-amount')[1].get_text().strip()
f.write('Number of users: ' + x + '\n')

# tabbable projpagetabs
x = soup.find_all(class_='badge badge-warning')[0].get_text().strip()
y = soup.find_all(class_='badge badge-warning')[1].get_text().strip()
z = soup.find_all(class_='badge badge-warning')[2].get_text().strip()
f.write('Updates: ' + x + ', Supporters: ' + y + ', Comments: ' + z + '\n')
f.write('=========================================================\n')

for x in list(soup.find_all('div', class_='panel panel-default')) + list(soup.find_all('div', class_='well')):
    try:
        y = x.find_all('strong')[0].get_text().strip() + ', ' + x.find_all('p')[0].get_text() + '\n'
        f.write(y)
        if y in data:
            index = data.index(y)
            del data[index]
        else:
            fn.write(y)
    except:
        y = x.find_all('p')[0].get_text() + '\n'
        f.write(y)
        if y in data:
            index = data.index(y)
            del data[index]
        else:
            fn.write(y)

f.close()
fn.close()
