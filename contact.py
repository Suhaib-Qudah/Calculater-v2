class Contact :

    def __init__(self,first_name,last_name,username,email):
        self.username= username
        self.first_name = first_name
        self.last_name = last_name
        self.id = id(self)
        self.email=list()
        self.phone_number=[]
        self.avatar_url=""
        self.friends=set()
        self.email.append(email)



    def set_username(self,username):
        self.username=username

    def set_f_name(self,first_name):
        self.first_name=first_name

    def set_l_name(self,last_name):
        self.last_name=last_name

    def set_email(self,email):
        self.email[0]=email


    def add_phone_num(self,phone_number):
        self.phone_numbers.append(phone_number)

    def get_user_name(self):
        return self.username

    def get_f_name(self):
        return self.first_name


    def get_l_name(self):
        return self.last_name

    def get_phone_number(self):
        return self.phone_number

    def get_email(self):
        return self.email[0]

 
