from tkinter import Tk,Frame,Label,Entry,Button,messagebox
from PIL import Image,ImageTk
import webbrowser
fonts = ('Times_New_Roman_Greek',15)
fontss = ('Times_New_Roman_Greek',23)
font3 = ('helvetica',8)
# font1 = ('Helvetica',18,'bold')

user_name_to_enter = 'a'
password_to_enter = '1'

root = Tk()
class Firstpage:
    def __init__(self,root):
        self.root = root
        self.page = Frame(self.root,width = 1000,height = 1000)
        self.page.place(x = 0, y = 0)


        self.image_logo = Image.open('../assets/img1.png')
        self.image_logo = self.image_logo.resize((920,820))
        self.image_logo = ImageTk.PhotoImage(self.image_logo)
        self.image_logo_label = Label(self.page,image = self.image_logo)
        self.image_logo_label.place(x = -100,y =-100)

        
        self.image_logos = Image.open('../assets/img2.png')
        self.image_logos = self.image_logos.resize((390,390))
        self.image_logos = ImageTk.PhotoImage(self.image_logos)
        self.image_logos_label = Label(self.page,image = self.image_logos,bg='black')
        self.image_logos_label.place(x = 180,y = 2)

        self.user_name = Label(self.page,text = 'User Name',bg = 'black',fg = 'white',font = fonts,width = 15,height = 2)
        self.user_name.place(x = 100,y = 300)
        self.user_name_entry = Entry(self.page,width = 30,font = fonts)
        self.user_name_entry.place(x = 300,y = 310)
        
        self.password = Label(self.page,text = 'Password',bg = 'black',fg = 'white',font = fonts,width = 15,height = 2)
        self.password.place(x = 100,y = 370)
        self.password_entry = Entry(self.page,width = 30,font = fonts)
        self.password_entry.place(x = 300,y = 380)
        
        self.button = Button(self.page ,text = 'login',font = fonts,width = 9,bg = 'white',fg='black',cursor='hand2',command =self.result)
        self.button.place(x = 330,y = 470)


    def result(self):
        global user_name_to_enter, password_to_enter
        self.bname = self.user_name_entry.get()
        self.aname = self.password_entry.get()
        if self.bname == user_name_to_enter and  self.aname == password_to_enter:
           self.page.destroy()
           sp = SecondPage(root)
        else:
            messagebox.showerror('INVALID','NO RESULT FOUND')
class SecondPage:
    def __init__(self,root):
        self.root = root
        self.root.title('INFO')
        self.page_1 = Frame(self.root,width = 1000,height = 1000)
        self.page_1.place(x = 0,y = 0)

        self.image_logoss = Image.open('../assets/img5.png')
        self.image_logoss = self.image_logoss.resize((920, 820))
        self.image_logoss = ImageTk.PhotoImage(self.image_logoss)
        self.image_logoss_label = Label(self.page_1, image=self.image_logoss)
        self.image_logoss_label.Image = self.image_logoss
        self.image_logoss_label.place(x=-100, y=-200)


        self.button_u = Button(self.page_1 ,text = 'Updates',font = fonts,width = 9,height = 1,bg = 'light steel blue',fg='black',cursor='hand2',command=self.on_updates)
        self.button_u.place(x = 16,y = 10)
 
        self.events = Label(self.page_1,text = ' Events ',bg = 'brown4',font = fonts,width = 13)
        self.events.place(x = 20,y = 80)

        self.button_up = Button(self.page_1 ,text = '+',font = fontss,width = 3,bg = 'black',fg='white',cursor='hand2')
        self.button_up.place(x = 670,y = 15)

        self.button_uu = Button(self.page_1 ,text = 'Chat \n Rooms',font = fonts,width = 10,height = 2,bg = 'black',fg='white',cursor='hand2')
        self.button_uu.place(x = 500,y = 15)
 

        self.button_e1 = Button(self.page_1 ,text = '<',font = fonts,bg = 'black',fg='white',cursor='hand2')
        self.button_e1.place(x = 30,y = 150)

        self.mylink_1=Label(self.page_1,text='Climate Ambition Summit',width =22 , height = 2,fg='white',bg='black',cursor='hand2',font=('Times',16))
        self.mylink_1.place(x=73,y=140)
        self.mylink_1.bind('<Button-1>',lambda x:webbrowser.open_new("https://www.greenclimate.fund/news/climate-ambition-summit-un-agencies-and-ifrc-kickstart-major-initiative-towards-realising-early"))

        self.mylink_2=Label(self.page_1,text='GreenPeace Volunteer',width =22 , height = 2,fg='white',bg='black',cursor='hand2',font=('Times',16))
        self.mylink_2.place(x=390,y=140)
        self.mylink_2.bind('<Button-1>',lambda x:webbrowser.open_new("https://www.greenpeace.org/india/en/volunteer-now/"))

        self.button_e1 = Button(self.page_1 ,text = '>',font = fonts,bg = 'black',fg='white',cursor='hand2')
        self.button_e1.place(x = 690,y = 150)


        self.button_e1 = Button(self.page_1 ,text = 'more',font = font3,width = 5,height=1,bg = 'dark green',fg='white',cursor='hand2',command=self.on_more_1)
        self.button_e1.place(x = 690,y = 210)

        self.events = Label(self.page_1,text = ' Petitions ',bg = 'brown4',font = fonts,width = 13)
        self.events.place(x = 20,y = 230)

        self.button_e1 = Button(self.page_1 ,text = '<',font = fonts,bg = 'black',fg='white',cursor='hand2')
        self.button_e1.place(x = 30,y = 300)

        self.mylink_p1=Label(self.page_1,text='Unjam Bengaluru',width =22 , height = 2,fg='white',bg='black',cursor='hand2',font=('Times',16))
        self.mylink_p1.place(x=73,y=290)
        self.mylink_p1.bind('<Button-1>',lambda x:webbrowser.open_new("https://www.greenpeace.org/india/en/unjam/?utm_content=Unjam&utm_campaign=Unjam_Bengaluru&utm_medium=direct&utm_source=website"))

        self.mylink_p1=Label(self.page_1,text='Nature Conservancy(climate)',width =22 , height = 2,fg='white',bg='black',cursor='hand2',font=('Times',16))
        self.mylink_p1.place(x=385,y=290)
        self.mylink_p1.bind('<Button-1>',lambda x:webbrowser.open_new("https://preserve.nature.org/page/81465/petition/1?locale=en-US"))

        self.button_e1 = Button(self.page_1 ,text = '>',font = fonts,bg = 'black',fg='white',cursor='hand2')
        self.button_e1.place(x = 690,y = 300)

        self.button_e1 = Button(self.page_1 ,text = 'more',font = font3,width = 5,height=1,bg = 'dark green',fg='white',cursor='hand2',command=self.on_more_2)
        self.button_e1.place(x = 690,y = 360)


        self.contr = Label(self.page_1,text = ' Contributions ',bg = 'brown4',font = fonts,width = 16)
        self.contr.place(x = 20,y = 380)

        self.button_e1 = Button(self.page_1 ,text = '<',font = fonts,bg = 'black',fg='white',cursor='hand2')
        self.button_e1.place(x = 30,y = 455)

        self.mylink_ce=Label(self.page_1,text='CoolEarth (donate)',width = 22, height = 2,fg='white',bg='black',cursor='hand2',font=('Times',16))
        self.mylink_ce.place(x=73,y=450)
        self.mylink_ce.bind('<Button-1>',lambda x:webbrowser.open_new("https://www.coolearth.org/donate/"))

        self.mylink_o=Label(self.page_1,text='Ocean Conservancy (donate)',width = 22, height = 2,fg='white',bg='black',cursor='hand2',font=('Times',16))
        self.mylink_o.place(x=390,y=450)
        self.mylink_o.bind('<Button-1>',lambda x:webbrowser.open_new("https://donate.oceanconservancy.org/page/92465/donate/1"))

        self.button_e1 = Button(self.page_1 ,text = '>',font = fonts,bg = 'black',fg='white',cursor='hand2')
        self.button_e1.place(x = 690,y = 455)

        self.button_e1 = Button(self.page_1 ,text = 'more',font = font3,width = 5,height=1,bg = 'dark green',fg='white',cursor='hand2',command=self.on_more_3)
        self.button_e1.place(x = 690,y = 510)

    def on_more_1(self):
        self.page_1.destroy()
        obj_classEvents = Events(root)

    def on_more_2(self):
        self.page_1.destroy()




    def on_more_3(self):
        self.page_1.destroy()
    

    def on_updates(self):
        self.page_1.destroy()
        obj_ClassUpdates = Updates(root)

class Events:
    def __init__(self,root):
        self.root=root
        self.root.title('Events')
        self.page_3 = Frame(self.root,width = 1000, height = 1000)
        self.page_3.place(x=0,y=0)

        self.image_1 = Image.open('../assets/img6.png')
        self.image_1 = self.image_1.resize((200, 200))
        self.image_1 = ImageTk.PhotoImage(self.image_1)
        self.image_1_label = Label(self.page_3, image=self.image_1)
        self.image_1_label.image = self.image_1
        self.image_1_label.place(x=50, y=30)

        self.mylink_z=Label(self.page_3,text='An Open Letter to the central pollution \n Control Board, we are Back!\n GreennPeace India \n October 3 2023',width = 32, height = 7,fg='white',bg='black',cursor='hand2',font=('Times',16))
        self.mylink_z.place(x=280,y=30)
        self.mylink_z.bind('<Button-1>',lambda x:webbrowser.open_new(("https://www.greenpeace.org/india/en/story/15290/an-open-letter-to-the-central-pollution-control-board-we-are-back/")))
        
        self.image_2 = Image.open('../assets/img7.png')
        self.image_2 = self.image_2.resize((220, 220))
        self.image_2 = ImageTk.PhotoImage(self.image_2)
        self.image_2_label = Label(self.page_3, image=self.image_2)
        self.image_2_label.image = self.image_2
        self.image_2_label.place(x=50, y=250)   
        

        self.mylink_z=Label(self.page_3,text='2023 UN Climate Change \n Conference (UNFCC COP 28)',width = 32, height = 7,fg='white',bg='black',cursor='hand2',font=('Times',16))
        self.mylink_z.place(x=280,y=250)
        self.mylink_z.bind('<Button-1>',lambda x:webbrowser.open_new(("https://sdg.iisd.org/events/2023-un-climate-change-conference-unfccc-cop-28/#:~:text=Event%3A%202023%20UN%20Climate%20Change,IISD&text=The%202023%20UN%20Climate%20Change,United%20Arab%20Emirates%20(UAE).")))
        

        self.button_e = Button(self.page_3 ,text = '  | \n V',font = fonts,bg = 'black',fg='white',cursor='hand2',height = 2)
        self.button_e.place(x = 350,y = 500)




class Updates:
    def __init__(self,root):
        self.root=root
        self.root.title('Updates')
        self.page_4 = Frame(self.root,width = 1000, height = 1000)
        self.page_4.place(x=0,y=0)

        self.image_3 = Image.open('../assets/img8.png')
        self.image_3 = self.image_3.resize((160, 140))
        self.image_3 = ImageTk.PhotoImage(self.image_3)
        self.image_3_label = Label(self.page_4, image=self.image_3)
        self.image_3_label.image = self.image_3
        self.image_3_label.place(x=50, y=30)

        self.mylink_z=Label(self.page_4,text='New Roman findings \n emerge from ruins amidst libyas \n tragic floods',width = 30, height = 6,fg='white',bg='black',cursor='hand2',font=('Times',16))
        self.mylink_z.place(x=280,y=30)
        self.mylink_z.bind('<Button-1>',lambda x:webbrowser.open_new(("https://economictimes.indiatimes.com/top-trending-products/news/amazon-great-indian-festival-massive-discounts-on-samsung-refrigerators-microwaves-washing-machines-and-acs/articleshow/104172875.cms ")))
        

        self.image_4 = Image.open('../assets/img9.png')
        self.image_4 = self.image_4.resize((160, 140))
        self.image_4 = ImageTk.PhotoImage(self.image_4)
        self.image_4_label = Label(self.page_4, image=self.image_4)
        self.image_4_label.image = self.image_4
        self.image_4_label.place(x=50, y=220)

        self.mylink_z=Label(self.page_4,text='India may lose 35 percent of\n  GDP to climate Change by\n 2100,warns Unescap report',width = 30, height = 6,fg='white',bg='black',cursor='hand2',font=('Times',16))
        self.mylink_z.place(x=280,y=200)
        self.mylink_z.bind('<Button-1>',lambda x:webbrowser.open_new(("https://m.economictimes.com/news/economy/indicators/india-may-lose-35-of-gdp-to-climate-change-by-2100-warns-unescap-report/articleshow/104222968.cms")))
        

        self.image_5 = Image.open('../assets/img10.png')
        self.image_5 = self.image_5.resize((160, 140))
        self.image_5 = ImageTk.PhotoImage(self.image_5)
        self.image_5_label = Label(self.page_4, image=self.image_5)
        self.image_5_label.image = self.image_5
        self.image_5_label.place(x=50, y=400)

        self.mylink_z=Label(self.page_4,text='Six Reasons why global \n temparatures are spiking right now',width = 30, height = 6,fg='white',bg='black',cursor='hand2',font=('Times',16))
        self.mylink_z.place(x=280,y=400)
        self.mylink_z.bind('<Button-1>',lambda x:webbrowser.open_new(("https://m.economictimes.com/news/science/six-reasons-why-global-temperatures-are-spiking-right-now/articleshow/104209402.cms ")))
        




        '''self.button1 = Button(self.page ,text = 'BACK',font = fonts,width = 9,bg = 'steel blue',command = self.back)
        self.button1.place(x = 330,y = 550)


    def back(self):
        global blank_to_enter
        self.bln = self.book_name_entry.get()
        if self.bln == blank_to_enter or self.bln == "  ":
           self.page.destroy()
           lib = Firstpage(root)
        else:
            messagebox.showerror('INVALID','NO RESULT FOUND')'''



root.geometry('750x600+400+100')
root.title('CLISOL')
fp = Firstpage(root)
root.mainloop()





