"""
تطبيق بيثون للأندرويد في ملف واحد
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import kivy
kivy.require('2.1.0')

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        # عنوان التطبيق
        title = Label(
            text='تطبيق بيثون للأندرويد',
            font_size=30,
            color=(0, 0.6, 0.8, 1)
        )
        
        # رسالة ترحيب
        message = Label(
            text='مرحباً بك في تطبيق بيثون!',
            font_size=20,
            color=(0.3, 0.3, 0.3, 1)
        )
        
        # زر تفاعلي
        self.counter = 0
        self.button = Button(
            text=f'اضغط هنا (تم الضغط 0 مرة)',
            size_hint=(0.8, 0.2),
            pos_hint={'center_x': 0.5},
            background_color=(0, 0.7, 0.3, 1)
        )
        self.button.bind(on_press=self.on_button_press)
        
        # إضافة العناصر
        layout.add_widget(title)
        layout.add_widget(message)
        layout.add_widget(self.button)
        
        return layout
    
    def on_button_press(self, instance):
        self.counter += 1
        if self.counter == 1:
            instance.text = f'اضغط هنا (تم الضغط {self.counter} مرة)'
        else:
            instance.text = f'اضغط هنا (تم الضغط {self.counter} مرات)'

if __name__ == '__main__':
    MyApp().run()
