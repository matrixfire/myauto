import openpyxl, re, time, random, sys, json, os, datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication 
from email.utils import formataddr
import traceback
import threading

import pyinputplus as pyip




class EmailClient:
    """ SMTP email client.
     connect and log in to an SMTP server, send an email, and disconnect from the server
      
        """
    def __init__(self, emailProvider, loginInfoList, sender_name='Bill'):
        self.emailProvider = emailProvider
        self.loginInfoList = loginInfoList
        self.sender = loginInfoList[0]
        self.sender_name = sender_name
        self.daily_capacity = 3
        self.emailCounter = 0
        self.aroused = False

        if not self.loginInfoList[0].startswith('bill'):
            self.sender_name = 'Alice'

        print(f'Email provider: {emailProvider}, email sender: {self.sender}')

    def connect(self):
        connection_settings = {
            'qq': ("smtp.qq.com", 170),
            'yahoo': ("smtp.mail.yahoo.com", 170),
            '163': ("smtp.163.com", 170),
            'qiye163': ("smtp.ym.163.com", 600),
            '126': ("smtp.126.com", 170),
            'tencent': ("smtp.exmail.qq.com", 170),
            'aol': ("smtp.aol.com", None),
            'sohu': ("smtp.sohu.com", None),
            'outlook': ("smtp-mail.outlook.com", 100),
            'gmail': ("smtp.gmail.com", None),
            'kingtrans': ("smtp.exmail.qq.com", 600),
            'cnkingtrans': ("smtp.exmail.qq.com", 600),
            'szkingtrans': ("smtp.qiye.aliyun.com", 500),
            'zohomail': ("smtp.zoho.com", 100),
            'yandex': ("smtp.yandex.ru", 100),
            'kaifang': ("smtp-n.global-mail.cn", 1000)
        }

        domain, capacity = connection_settings.get(self.emailProvider, (None, None))
        if domain:
            self.connectSSL(domain)
            if capacity:
                self.daily_capacity = capacity

        print(f'{self.sender}: connected')

    
    def connectTLS(self, smtpDomain):
        self.smtpObj = smtplib.SMTP(smtpDomain, 587) # Connecting to an SMTP Server
        self.smtpObj.ehlo() # Sending the SMTP “Hello” Message
        self.smtpObj.starttls() # Starting TLS Encryption

    def connectSSL(self, smtpDomain):
        '''If the smptlib.SMTP() call is not successful, your SMTP server might not support TLS on port 587. 
        In this case, you will need to create an SMTP object using smtplib.SMTP_SSL() and port 465 instead.'''
        self.smtpObj = smtplib.SMTP_SSL(smtpDomain, 465)
        self.smtpObj.ehlo()

    def login(self):
        mail_user = self.loginInfoList[0]
        mail_password = self.loginInfoList[1]
        if mail_password == '':
            mail_password = pyip.inputPassword('Password for email: ')
        try:
            self.smtpObj.login(mail_user, mail_password) # Logging In to the SMTP Server
            print(f'{self.sender}: logged in')
        except:
            print(f'{self.sender}, login failed')

    def send(self, from_address, to_address, msg):
        self.smtpObj.sendmail(from_address, to_address, msg) # Sending an Email
        self.emailCounter += 1

    def disconnect(self):
        self.smtpObj.quit() # Sending an Email
        print('Email SMTP server quitted!')



class EmailContents:
    """
    Handles retrieving email messages and titles from templates.
    """
    def __init__(self, titleList, msgList, multi=1):
        self.titles = titleList
        self.messages = msgList
        self.multi = multi

    def get_message(self):
        return self.get_first_message() if self.multi == 1 or self.multi == '' else self.get_any_message()

    def get_title(self):
        return self.get_first_title() if self.multi == 1 or self.multi == '' else self.get_any_title()

    def get_first_message(self):
        return self.messages[0]

    def get_first_title(self):
        return self.titles[0]

    def get_any_message(self):
        return random.choice(self.messages)

    def get_any_title(self):
        return random.choice(self.titles)


def get_stored_info(json_history_file):
    """
    Retrieves a list containing emails sent, stored in a JSON file.
    """
    filename = os.path.join('temp_email', json_history_file)
    print('SAVE FILE TO', filename)
    try:
        with open(filename) as f:
            emailsSent = json.load(f)
    except FileNotFoundError:
        print(f'Json file: {json_history_file} not found')
        return []
    else:
        if 'yahoo' in json_history_file:
            print('YAHOO EMAIL HISTORY', emailsSent)
        return emailsSent


def save_email_history(email, emailsSent, json_history_file):
    """
    Saves the emails list back to the JSON file.
    """
    current_time = datetime.datetime.now()
    time_str = f'{current_time.year}-{current_time.month}-{current_time.day}'
    filename = os.path.join('temp_email', json_history_file)
    print(f'Email({email}) saved in json file.')
    emailsSent.append((email, time_str))
    with open(filename, 'w') as f:
        json.dump(emailsSent, f)



def extractDataFromExcel(templatefile, sheetNumber):
    """
    Returns a list containing data extracted from an Excel workbook.
    """
    try:
        wb = openpyxl.load_workbook(templatefile)
        print(f'Sheet names list: {wb.sheetnames}')
        sheet = wb[wb.sheetnames[sheetNumber - 1]]

        cache_list = []
        for i in range(2, sheet.max_row + 1):  # Go through every row
            temp_list_for_row = []
            for j in range(1, sheet.max_column + 1):
                temp_list_for_row.append(sheet.cell(row=i, column=j).value)
            cache_list.append(temp_list_for_row)
        return cache_list
    except Exception as e:
        print('Make sure the excel template exists:', str(e))
        sys.exit()


def autoEmail(emailClient, email, title, msg, emailsSent, json_history_file):
    """
    Sends an email using specified client settings, appends the sender signature, and logs the history.
    Parameters:
        emailClient (EmailClient): The email client instance used for sending emails.
        email (str): The recipient's email address.
        title (str): The subject line of the email.
        msg (str): The body of the email.
        emailsSent (list): A list of sent emails to be logged.
        json_history_file (str): The filename for storing email log history.
    """
    sender = emailClient.sender
    sender_name = emailClient.sender_name

    if 'notyet54321' not in msg:
        msg += f"\nRegards\n{sender_name}\nKingtrans Container Line(Shenzhen) CO., LTD"

    m = MIMEText(msg, 'plain', 'utf8')
    m['From'] = sender
    m['To'] = email
    m['Subject'] = title

    try:
        sendmailStatus = emailClient.server.sendmail(sender, email, m.as_string())
    except smtplib.SMTPServerDisconnected:
        print(f'{emailClient.sender} caught it: disconnect!!')
        emailClient.connect()
        emailClient.login()
        sendmailStatus = emailClient.send(sender, email, m.as_string())

    if sendmailStatus:
        print(f'{emailClient.sender}: There was a problem sending email to {email}: {sendmailStatus}')
    else:
        print('-' * 100)
        print(f'Title: {title}, {sender} -> {email}')
        print(msg)
        print(f'\n{sender} -> {email}: {title} - ok')
        current_time = datetime.datetime.now()
        print(f"{current_time.strftime('%H:%M:%S')}")
        print('-' * 100)
        save_email_history(email, emailsSent, json_history_file)


def emailProcess(infoFromExcel, emailClient, emailContents):
    """
    Processes the email sending operation from a list of extracted Excel data.
    Parameters:
        infoFromExcel (list): A list of data extracted from an Excel file.
        emailClient (EmailClient): The client object that manages email sending operations.
        emailContents (EmailContents): An object to manage retrieval of message and title templates.
    """
    global global_counter, timeInterval
    print('work!')
    time.sleep(3.7)
    print('Debug:!!!!!', timeInterval)

    cache_list = infoFromExcel
    print('Extracted info done.')
    print("Rows: ", len(cache_list))

    json_history_file = f"{emailClient.sender.split('@')[0]}-{emailClient.emailProvider}.json"
    print('Json file is located at:', json_history_file)
    emailsSent = get_stored_info(json_history_file)
    emailsSentAdd = [e_tuple[0] for e_tuple in emailsSent]

    daily_counter = 0
    for i, row_data in enumerate(cache_list, start=1):
        mutex.acquire()
        global_counter += 1
        mutex.release()

        # Initialize dictionary for formatting email content
        d = {f'f{index + 1}': content if content else '' for index, content in enumerate(row_data)}

        # Detect which field is the email
        email = d['f1']
        if email in emailsSentAdd and email != '349500371@qq.com':
            print(f'Email No.{i}: {email} already sent.')
            continue

        daily_counter += 1
        if daily_counter >= emailClient.daily_capacity + 1:
            print('May have reached daily capacity.')
            break

        message_text = emailContents.get_message()
        subject_text = emailContents.get_title()
        msg = message_text.format(**d)
        title = subject_text.format(**d)

        if timeInterval == 0:
            time2sleep = random.randint(1, 80)
        else:
            timeInterval = max(timeInterval, 12)
            time2sleep = timeInterval + random.randint(1, 10)

        try:
            autoEmail(emailClient, email, title, msg, emailsSent, json_history_file)
            print(f'Email No.{i} (global: {global_counter}) finished, sleep for {time2sleep}s')
            lucky_wait = 0
            r = random.randint(1, 100)
            if r <= 2:
                lucky_wait = 1000
            elif r <= 5:
                lucky_wait = 500
            elif r <= 10:
                lucky_wait = 200
            elif r <= 30:
                lucky_wait = 30
            elif r <= 50:
                lucky_wait = 10
            print(f'Luckily waiting for {lucky_wait}s')
            time.sleep(lucky_wait)
            
            if i == len(cache_list):
                print('Email task finished.')
                sys.exit(0)
            time.sleep(time2sleep)
        except Exception as e:
            print(f'{emailClient.sender}: {email} failed, error is: {e}')
            time.sleep(1)

    

def get_num(jsondata):
    """
    Calculate the number of emails sent on the current day based on the json data.
    Parameters:
        jsondata (list): List of tuples containing email information.
    Returns:
        int: The number of emails sent today.
    """
    current_time = datetime.datetime.now()
    time_str = f'{current_time.year}-{current_time.month}-{current_time.day}'
    return sum(1 for email_tuple in jsondata if email_tuple[1] == time_str)


def getAccountInfo(myAccounts):
    """
    Generate a dictionary of accounts and the number of emails sent today.
    Parameters:
        myAccounts (list): List of accounts to check.
    Returns:
        dict: A dictionary mapping each email account to the number of emails sent today.
    """
    result_dict_raw = {acc[0]: get_stored_info(f"{acc[0].split('@')[0]}-{acc[-1]}.json") for acc in myAccounts}
    return {email: get_num(jsondata) for email, jsondata in result_dict_raw.items()}


def ask(myAccounts, templatefile):
    """
    Interactively ask the user to choose an email account and Excel tab for email processing.
    Parameters:
        myAccounts (list): List of email accounts available.
        templatefile (str): Path to the Excel template file.
    Returns:
        tuple: Selected email account, domain name, Excel tab ID, and messaging mode.
    """
    sheets = openpyxl.load_workbook(templatefile).sheetnames
    result_dict = getAccountInfo(myAccounts)

    for i, acc in enumerate(myAccounts):
        print(f'Enter {i+1} for {acc[0]}, emails already sent today: {result_dict[acc[0]]}')

    multiMsg = pyip.inputNum(prompt='Enter mode (Empty or 1 for single, 2 for multiple, 3-5 for groups): ', blank=True, min=1, max=5)
    emailAcc, emailDomainName = None, None
    if multiMsg not in [3, 4, 5]:
        num = pyip.inputNum('Email account number:', min=1, lessThan=len(myAccounts) + 1)
        emailAcc = myAccounts[num - 1]
        emailDomainName = emailAcc[2]  # Or use split method on emailAcc[0] as needed.

    for i, tab in enumerate(sheets):
        print(f'Enter {i+1} for {tab}')
    excelTabId = pyip.inputNum(f'Enter tab ID 1-{len(sheets)}: ', min=1, lessThan=len(sheets) + 1)

    return emailAcc, emailDomainName, excelTabId, multiMsg




# initial settings

qq = ['amazingtransition1@qq.com', 'lzeigqinjesxbegg', 'qq']
qq2 = ['349500371@qq.com', 'fuutvkptczbrbhcd', 'qq']
qq3 = ['mangocutting@qq.com', 'znczqetqojqidcfa', 'qq']
qq4 = ['divideandconquer@qq.com', 'mbabhgdhdchdbhhh', 'qq']
qq5 = ['475853055@qq.com', 'vvwzavwulcvybhib', 'qq']


# e163 = ['matrixbox@163.com', 'GWNRCXEXINIVGQQA', '163']
E163 = ['mangocutting@163.com', 'EXXUDFPSVFXHPASH', '163']
ee1_163 = ['ivoq1690cb@163.com', 'ex535491', '163']
ee2_163 = ['tgraed451pql@163.com', 'sv620835', '163']


yahoo = ['matrixbox@yahoo.com', 'vtioleoeammkhhuy', 'yahoo']
# yahoo2 = ['greatinequality@yahoo.com', 'cvxvttvowldnyazz']

tencent = ['bill.zou@kingtrans.com.cn', 'Ks2022', 'kingtrans']



ali = ['bill.zou@szkingtrans.com', 'Alihtam51409', 'szkingtrans']

tencent2 = ['sales06@cnkingtrans.com', 'Tthtam51409', 'cnkingtrans']
qy163 = ['sales06@kingtrans.cc', 'kingtrans123', 'qiye163']
newEmail1 = ['sales06@kingtrans.ltd', 'Elhtam51409', 'kaifang']
newEmail2 = ['sales09@kingtrans.ltd', 'Elhtam51409', 'kaifang']


# mix = ['bill@mix.com', 'mix']
yandex1 = ['whynotbinary@yandex.com', 'lgmflbuqtqqozhkp', 'yandex']
# yandex2 = ['recursivedream@yandex.com', 'azxffljchocjwjex', 'yandex'] # may spam
# yandex3 = ['greatiteration@yandex.com', 'rreekalaxwugdqhn', 'yandex']  # may spam


e126 = ['recursivesolution@126.com', 'GWRQEDXRJEROECVO']
aol = ['binarysearch01@aol.com', 'kiahlbyxmempunlc']
sohu = ['binarysearch01@sohu.com', 'L01KRIHMFTO']
outlook = ['recursivedream@outlook.com', ''] #300 emails zhantingle! no use!
outlook2 = ['algorithmfuture@outlook.com', 'Elhtam51409'] #300 emails
gmail = ['mangocutting@gmail.com', 'ynfobiwnrcpnrelj']
e139 = ['matrixfire@139.com', 'b8e20770c1597ccb2000']



gmail2 = ['zmeng049@gmail.com', 'BILL0415', 'gmail']

# zohomail = ['matrixbox@zohomail.com', 'YLN4rvqeZNJx']

'''ivoq1690cb@163.com----ex535491
tgraed451pql@163.com----sv620835'''

myAccounts = []
myAccounts.append(tencent)
myAccounts.append(ali)
myAccounts.append(tencent2)
myAccounts.append(qq)    
myAccounts.append(qq2)
myAccounts.append(qq3)    
myAccounts.append(qq4)    
myAccounts.append(qq5)      
myAccounts.append(yahoo)    
myAccounts.append(qy163)
myAccounts.append(newEmail1)
myAccounts.append(newEmail2)

myAccounts.append(gmail2)
groupA = [tencent2, ali, tencent] # 3
groupB = [qq, qq2, qq3, qq4, qq5] # , yahoo] 4
groupC = [tencent, newEmail2] #, yandex1, outlook2] 5 qy163, 




def emailWork(emailClient, infoFromExcel):
    """
    Manages the entire email sending workflow from connecting to sending and disconnecting.
    Parameters:
        emailClient (EmailClient): The email client instance to manage connections and sending.
        infoFromExcel (list): List of extracted email information from Excel.
    """
    emailContents = EmailContents(titleList=subject_texts, msgList=message_texts, multi=multiMsg)
    print('Template Info extracted!')
    print('timeInterval is', timeInterval)

    try:
        emailClient.connect()
        emailClient.login()
        emailProcess(infoFromExcel, emailClient, emailContents)
        emailClient.disconnect()
    except Exception as e:
        print('Failed in the first attempt!', e)
        emailClient.connect()
        emailClient.login()
        emailProcess(infoFromExcel, emailClient, emailContents)
        emailClient.disconnect()


def divideList2Parts(alist, parts=2):
    """
    Divides a list into the specified number of parts.
    Parameters:
        alist (list): The list to divide.
        parts (int): The number of parts to divide the list into.
    Returns:
        dict: A dictionary with parts as keys and list segments as values.
    """
    temp_dict = {i: [] for i in range(parts)}
    for i, v in enumerate(alist):
        temp_dict[i % parts].append(v)
    return temp_dict

def muiltiEmails(infoFromExcel, group):
    """
    Manages sending emails using multiple threads, each handling a part of the list.
    Parameters:
        infoFromExcel (list): A list of email information extracted from Excel.
        group (list): A list of email account groups.
    """
    group_dict = divideList2Parts(infoFromExcel, len(group))
    thread_list = []
    for i, emailAccounts in enumerate(group):
        thisEmailClient = EmailClient(emailAccounts[-1], emailAccounts)
        thread = threading.Thread(target=emailWork, args=(thisEmailClient, group_dict[i]))
        thread_list.append(thread)

    for thread in thread_list:
        time.sleep(5)  # Controlled start delay to avoid sudden surge
        thread.start()







if __name__ == '__main__':
    # Initialize global counter and mutex for thread synchronization
    global_counter = 0
    mutex = threading.Lock()

    # Define base directory and file paths
    base_dir = 'temp_email'
    templatefile_name = 'email_auto.xlsx'
    templatefile = os.path.join(base_dir, templatefile_name)


    # User interaction to determine processing parameters
    emailAcc, emailDomainName, excelTabId, multiMsg = ask(myAccounts, templatefile)
    print('multiMsg is', multiMsg)

    # Retrieve template information and extract data from Excel
    message_texts, subject_texts, timeInterval = getTemplateInfo(contentTemplate, multiMsg) # ？？？？



    infoFromExcel = extractDataFromExcel(templatefile, excelTabId)

    # Process emails based on the specified mode
    if multiMsg in [1, 2] or multiMsg == '':
        emailClient = EmailClient(emailDomainName, emailAcc)
        emailWork(emailClient, infoFromExcel)
    elif multiMsg == 3:  # groupA
        print(f'{multiMsg} means: Entering groupA')
        muiltiEmails(infoFromExcel, groupA)
    elif multiMsg == 4:  # groupB
        print(f'{multiMsg} means: Entering groupB')
        muiltiEmails(infoFromExcel, groupB)
    elif multiMsg == 5:  # groupC
        print(f'{multiMsg} means: Entering groupC')
        muiltiEmails(infoFromExcel, groupC)




'''
Notes:

import itertools

list1 = [1, 2]
list2 = ['a', 'b']
perms = list(itertools.permutations(list1))
product = list(itertools.product(list1, list2))



'''