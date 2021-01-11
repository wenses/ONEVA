import kivy
from kivy.app import App 
from kivy.core.window import Window 
from kivy.uix.label import Label 
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.screenmanager import Screen, ScreenManager 
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput 
#from kivy.uix.image import Image 

Window.clearcolor=(20/255.0,20/255.0,20/255.0,1)

class Main(GridLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.cols=1
		#self.add_widget(Label())
		self.title=Label(text='ONEVA',color=(0,1,0,1),pos=(350,500),font_size=35)
		self.add_widget(self.title)
		self.add_widget(Label())

		self.add_widget(Label(text='ONLINE NATIONAL ELECTION VOTING APP',color=(0,1,0,1),font_size=20))

		self.add_widget(Label())
		self.start_button=Button(text='START',background_color=(0,500/255.0,0,1))
		self.start_button.bind(on_press=self.goingto_start)
		self.add_widget(self.start_button)

		self.about_button=Button(text='ABOUT AND HOW TO USE',background_color=(0,500/255.0,0,1))
		self.about_button.bind(on_press=self.goingto_about)
		self.add_widget(self.about_button)

	def goingto_start(self, instance):
		oneva.sm.current='start'

	def goingto_about(self, instance):
		oneva.sm.current='about'

class Start(GridLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.cols=2

		self.add_widget(Label(text='ENTER THE ',color=(0,1,0,1)))
		self.add_widget(Label(text='REQUIREMENTS BELOW',color=(0,1,0,1)))

		#Full Name
		self.add_widget(Label(text='Enter your full name: ',color=(0,1,0,1)))
		self.full_name=TextInput(multiline=False)
		self.add_widget(self.full_name)

		#NIDA card number
		self.add_widget(Label(text='NIDA card number: ',color=(0,1,0,1)))
		self.nida_no=TextInput(multiline=False)
		self.add_widget(self.nida_no)

		#Year of birth
		self.add_widget(Label(text='Enter year of birth: ',color=(0,1,0,1)))
		self.yr=TextInput(multiline=False)
		self.add_widget(self.yr)


		#self.add_widget(Label())

		self.back=Button(text='GO BACK',background_color=(0,500/255.0,0,1))
		self.back.bind(on_press=self.gb)
		self.add_widget(self.back)

		self.submit=Button(text='SUBMIT',background_color=(0,500/255.0,0,1))
		self.submit.bind(on_press=self.submitting)
		self.add_widget(self.submit)

	def submitting(self, instance):
		name=self.full_name.text 
		nida=self.nida_no.text 
		year=self.yr.text 
		if name=='twm' and nida=='1234' and year=='2005':
			#self.add_widget(Label(text='IT WORKED GO AND VOTE',color=(0,1,0,1)))
			oneva.sm.current='voting'
		elif name=='Ignace Amani Mchallo' and nida=='12345' and year=='1956':
			oneva.sm.current='voting'
		else:
			#oneva.sm.current='main'
			oneva.sm.current='voting'
	def gb(self, instance):
		oneva.sm.current='main'

class Voting(GridLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.cols=2

		self.add_widget(Label(text="CHOOSE WHOM YOU WANT",color=(0,1,0,1)))
		self.add_widget(Label(text="TO VOTE FOR BELOW",color=(0,1,0,1)))
		self.add_widget(Label())
		self.add_widget(Label())
		#self.add_widget(Label())
		#self.add_widget(Label())

		self.add_widget(Label(text='MAGUFULI',color=(0,1,0,1),font_size=20))
		self.add_widget(Label(text='LISSU',color=(0,1,0,1),font_size=20))
		#self.add_widget(CheckBox(color=(0,1,0,1)))
		#self.add_widget(CheckBox(color=(0,1,0,1)))
		self.f=CheckBox(color=(0,1,0,1))
		self.add_widget(self.f)
		self.f1=CheckBox(color=(0,1,0,1))
		#self.f1.bind(on_press=self.check)
		self.add_widget(self.f1)

		self.magufuli=Button(text='VOTE MAGUFULI',background_color=(0,500/255.0,0,1))
		#self.add_widget(self.magufuli)
		self.lissu=Button(text='VOTE LISSU',background_color=(0,500/255.0,0,1))
		#self.add_widget(self.lissu)

		self.back=Button(text='GO BACK',background_color=(0,500/255.0,0,1))
		self.back.bind(on_press=self.gh)
		self.add_widget(self.back)

		self.fisrst=CheckBox()
		#self.add_widget(self.fisrst)

		self.nothing=Button(text='SUBMIT',background_color=(0,500/255.0,0,1))
		self.nothing.bind(on_press=self.check)
		self.add_widget(self.nothing)

	def check(self, instance):
		#oneva.sm.current='main'
		#self.add_widget(Label(text='TOO BAD! HE LOST',color=(1,0,0,1)))
		if self.f.active:
			self.add_widget(Label(text='WON',color=(0,1,0,1)))
			ans='MAGUFULI'
			fmsg=f'Thank you for using ONEVA to choose {ans}'
			oneva.finish.update(fmsg)
			oneva.sm.current='finish'
		elif self.f1.active:
			self.add_widget(Label(text='LOST',color=(1,0,0,1)))
			ans='LISSU'
			fmsg=f'Thank you for using ONEVA to choose {ans}'
			oneva.finish.update(fmsg)
			oneva.sm.current='finish'

	def gh(self, instance):
		oneva.sm.current='main'

		#self.add_widget(Label())
		#self.add_widget(Label())

class Finish(GridLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.cols=1

		self.message=Label(halign='center',font_size=27,color=(0,1,0,1))
		self.add_widget(self.message)

		self.add_widget(Label())
		self.add_widget(Label())
		self.add_widget(Label())

		self.exit_button=Button(text='EXIT',background_color=(0,500/255.0,0,1))
		self.exit_button.bind(on_press=self.ex)
		self.add_widget(self.exit_button)



	def update(self,message):
		self.message.text=message

	def ex(self, instance):
		exit()


class About(GridLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.cols=1

		with open('about.txt','r') as f:
			about_info=f.read()

		self.info=Label(text=about_info,color=(0,1,0,1))
		self.add_widget(self.info)

		self.add_widget(Label())
		#self.add_widget(Label())

		self.g=Button(text='GO BACK',background_color=(0,500/255.0,0,1))
		self.g.bind(on_press=self.gh)
		self.add_widget(self.g)

		

	def gh(self, instance):
		oneva.sm.current='main'



class ONEVAApp(App):
	def build(self):
		self.sm=ScreenManager()

		self.main=Main()
		screen=Screen(name='main')
		screen.add_widget(self.main)
		self.sm.add_widget(screen)

		self.start=Start()
		screen=Screen(name='start')
		screen.add_widget(self.start)
		self.sm.add_widget(screen)

		self.voting=Voting()
		screen=Screen(name='voting')
		screen.add_widget(self.voting)
		self.sm.add_widget(screen)

		self.about=About()
		screen=Screen(name='about')
		screen.add_widget(self.about)
		self.sm.add_widget(screen)

		self.finish=Finish()
		screen=Screen(name='finish')
		screen.add_widget(self.finish)
		self.sm.add_widget(screen)

		return self.sm

if __name__=='__main__':
	oneva=ONEVAApp()
	oneva.run()
