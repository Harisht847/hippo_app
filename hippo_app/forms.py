from django import forms


def get_db_names():
    DB_NAMES = ()
    pass



DB_NAMES = (
    ('', 'Choose...'),
    ('sql', 'sql'),
    ('mysql', 'mysql'),
    ('oracle', 'oracle')
)

DATABASE= (
    ('', 'Choose'),
    ('DB1', 'DB1'),
    ('DB2', 'DB2'),
    ('DB3', 'DB3')
)


TABLES = (
    ("Table1", "Table1"),
    ("Table2", "Table2"),
    ("Table3","Table3")
)


class MigrationForm(forms.Form):
    Source = forms.ChoiceField(choices = DB_NAMES)
    username = forms.CharField(widget=forms.TextInput(attrs = {'placeholder' : 'Email'}))
    password = forms.CharField(widget = forms.PasswordInput())
    host =  forms.CharField(label = 'host')
    DataBases = forms.ChoiceField(choices = DATABASE)
    Tables = forms.ChoiceField(choices = TABLES)    

    '''
    address_1 = forms.CharField(label = 'Address', widget = forms.TextInput(attrs = {'placeholder':'1234 main st'}))
    address_2 = forms.CharField(label = 'Address', widget = forms.TextInput(attrs = {'placeholder':'1234 main st'}))
    city = forms.CharField()
    
    zip_code = forms.CharField(label = 'zip')
    check_me_out = forms.BooleanField(required=False)
    '''


class MigrationForm2(forms.Form):
    destination = forms.ChoiceField(choices = DB_NAMES)
    account = forms.CharField()
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput())
    role = forms.CharField()
    warehouse = forms.CharField()
    database = forms.CharField()
    schema = forms.CharField()
