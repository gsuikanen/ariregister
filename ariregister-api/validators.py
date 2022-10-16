import datetime

def validateCompanyData(data):
    validationErrors = ''
    #Name validation: 3-100 symbols
    try:
        companyName = data['companyName']
        if len(companyName) < 3 or len(companyName) > 100:
            validationErrors = validationErrors + 'Company name should be 3-100 symbols long\n'
    except:
        validationErrors = validationErrors + 'Company name missing\n'
    #Company code validation: 7-digit
    try:
        companyCode = data['companyCode']
        if len(companyCode) != 7:
            validationErrors = validationErrors + 'Company code should consist of 7 numbers\n'
        companyCode = int(companyCode)
    except:
        validationErrors = validationErrors + 'Company code should consist of 7 numbers\n'
    #Company registration date validation: not in future
    try:
        companyRegdt = datetime.datetime.strptime(data['companyRegdt'], '%Y-%m-%d').date()
        if companyRegdt > datetime.date.today():
            validationErrors = validationErrors + 'Company registration date can not be in future\n'
    except:
        validationErrors = validationErrors + 'Company registration date missing\n'
    #Owners validation: at least 1 owner
    try:
        owners = data['owners']
        if len(owners) < 1:
            validationErrors = validationErrors + 'Please add at least one owner\n'
    except:
        validationErrors = validationErrors + 'Company owners missing\n'
    #Total capital validation: at least 2500
    try:
        totalCapital = 0
        for own in owners:
            totalCapital = totalCapital + int(own['ownerCapital'])
        if totalCapital < 2500:
            validationErrors = validationErrors + 'Company capital should be at least 2500\n'
    except:
        validationErrors = validationErrors + 'Company capital missing\n'
    return validationErrors



def validateOwners(owners):
    dict_out = {}
    i = 0
    while i < len(owners):
        own = owners[i]
        err = validateOwner(own)
        if err != '':
            dict_out[i] = err
        i += 1
    return dict_out

def validateOwner(own):
    validationErrors = ''
    try:
        if own['ownerName'] == '':
            validationErrors = validationErrors + 'Owner name is empty\n'
        if own['ownerType'] == 'priv' and own['ownerSurname'] == '':
            validationErrors = validationErrors + 'Owner surname is empty\n'
        if own['ownerCode'] == '':
            validationErrors = validationErrors + 'Owner code is empty\n'
        if int(own['ownerCapital']) < 0:
            validationErrors = validationErrors + 'Capital should be at least 1 euro\n'
    except:
        validationErrors = 'Owner data is incorrect'
    return validationErrors