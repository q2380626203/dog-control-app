import os
import platform
import sys
import time

# Setup library path for SDK
arch = platform.machine().replace('amd64', 'x86_64').replace('arm64', 'aarch64')
lib_path = os.path.abspath(f'{os.path.dirname(__file__)}/zsibot_sdk/lib/zsl-1/{arch}')
sys.path.insert(0, lib_path)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.core.window import Window

try:
    import mc_sdk_zsl_1_py
    SDK_AVAILABLE = True
except ImportError:
    SDK_AVAILABLE = False


class DogControlApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dog = None
        self.connected = False
        self.log_text = ""

    def build(self):
        Window.clearcolor = (0.95, 0.95, 0.95, 1)

        # 主布局
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 标题
        title = Label(
            text='机器狗语音控制',
            size_hint=(1, 0.1),
            font_size='24sp',
            color=(0.2, 0.2, 0.2, 1)
        )
        main_layout.add_widget(title)

        # 连接配置区域
        self.setup_connection_ui(main_layout)

        # 控制按钮区域
        self.setup_control_ui(main_layout)

        # 日志显示区域
        self.setup_log_ui(main_layout)

        return main_layout

    def setup_connection_ui(self, parent):
        """设置连接配置界面"""
        conn_box = BoxLayout(orientation='horizontal', size_hint=(1, 0.1), spacing=5)

        # 本地IP输入
        conn_box.add_widget(Label(text='本地IP:', size_hint=(0.2, 1), color=(0, 0, 0, 1)))
        self.local_ip_input = TextInput(
            text='192.168.234.9',
            multiline=False,
            size_hint=(0.3, 1)
        )
        conn_box.add_widget(self.local_ip_input)

        # 机器狗IP输入
        conn_box.add_widget(Label(text='机器狗IP:', size_hint=(0.2, 1), color=(0, 0, 0, 1)))
        self.dog_ip_input = TextInput(
            text='192.168.234.1',
            multiline=False,
            size_hint=(0.3, 1)
        )
        conn_box.add_widget(self.dog_ip_input)

        parent.add_widget(conn_box)

        # 连接按钮
        self.connect_btn = Button(
            text='连接机器狗',
            size_hint=(1, 0.08),
            background_color=(0.2, 0.6, 1, 1)
        )
        self.connect_btn.bind(on_press=self.connect_dog)
        parent.add_widget(self.connect_btn)

    def setup_control_ui(self, parent):
        """设置控制按钮界面"""
        control_label = Label(
            text='控制命令',
            size_hint=(1, 0.06),
            color=(0.2, 0.2, 0.2, 1),
            font_size='18sp'
        )
        parent.add_widget(control_label)

        # 基础控制按钮
        basic_grid = BoxLayout(orientation='horizontal', size_hint=(1, 0.12), spacing=5)

        btn_standup = Button(text='站起来', background_color=(0.3, 0.7, 0.3, 1))
        btn_standup.bind(on_press=lambda x: self.execute_command('standup'))
        basic_grid.add_widget(btn_standup)

        btn_liedown = Button(text='趴下', background_color=(0.7, 0.5, 0.3, 1))
        btn_liedown.bind(on_press=lambda x: self.execute_command('liedown'))
        basic_grid.add_widget(btn_liedown)

        parent.add_widget(basic_grid)

        # 移动控制按钮
        move_grid = BoxLayout(orientation='horizontal', size_hint=(1, 0.12), spacing=5)

        btn_forward = Button(text='前进', background_color=(0.2, 0.5, 0.8, 1))
        btn_forward.bind(on_press=lambda x: self.execute_command('forward'))
        move_grid.add_widget(btn_forward)

        btn_backward = Button(text='后退', background_color=(0.2, 0.5, 0.8, 1))
        btn_backward.bind(on_press=lambda x: self.execute_command('backward'))
        move_grid.add_widget(btn_backward)

        btn_left = Button(text='左移', background_color=(0.2, 0.5, 0.8, 1))
        btn_left.bind(on_press=lambda x: self.execute_command('left'))
        move_grid.add_widget(btn_left)

        btn_right = Button(text='右移', background_color=(0.2, 0.5, 0.8, 1))
        btn_right.bind(on_press=lambda x: self.execute_command('right'))
        move_grid.add_widget(btn_right)

        parent.add_widget(move_grid)

        # 旋转控制按钮
        turn_grid = BoxLayout(orientation='horizontal', size_hint=(1, 0.12), spacing=5)

        btn_turn_left = Button(text='左转', background_color=(0.5, 0.4, 0.7, 1))
        btn_turn_left.bind(on_press=lambda x: self.execute_command('turn_left'))
        turn_grid.add_widget(btn_turn_left)

        btn_turn_right = Button(text='右转', background_color=(0.5, 0.4, 0.7, 1))
        btn_turn_right.bind(on_press=lambda x: self.execute_command('turn_right'))
        turn_grid.add_widget(btn_turn_right)

        parent.add_widget(turn_grid)

        # 特技动作按钮
        trick_grid = BoxLayout(orientation='horizontal', size_hint=(1, 0.12), spacing=5)

        btn_jump = Button(text='跳跃', background_color=(0.8, 0.3, 0.3, 1))
        btn_jump.bind(on_press=lambda x: self.execute_command('jump'))
        trick_grid.add_widget(btn_jump)

        btn_front_jump = Button(text='前跳', background_color=(0.8, 0.3, 0.3, 1))
        btn_front_jump.bind(on_press=lambda x: self.execute_command('front_jump'))
        trick_grid.add_widget(btn_front_jump)

        btn_backflip = Button(text='后空翻', background_color=(0.8, 0.3, 0.3, 1))
        btn_backflip.bind(on_press=lambda x: self.execute_command('backflip'))
        trick_grid.add_widget(btn_backflip)

        btn_shake_hand = Button(text='握手', background_color=(0.8, 0.3, 0.3, 1))
        btn_shake_hand.bind(on_press=lambda x: self.execute_command('shake_hand'))
        trick_grid.add_widget(btn_shake_hand)

        parent.add_widget(trick_grid)

    def setup_log_ui(self, parent):
        """设置日志显示界面"""
        log_label = Label(
            text='运行日志',
            size_hint=(1, 0.05),
            color=(0.2, 0.2, 0.2, 1),
            font_size='16sp'
        )
        parent.add_widget(log_label)

        # 日志显示区域
        scroll = ScrollView(size_hint=(1, 0.25))
        self.log_display = Label(
            text='等待连接...',
            size_hint_y=None,
            color=(0, 0, 0, 1),
            halign='left',
            valign='top'
        )
        self.log_display.bind(texture_size=self.log_display.setter('size'))
        scroll.add_widget(self.log_display)
        parent.add_widget(scroll)

    def add_log(self, message):
        """添加日志信息"""
        timestamp = time.strftime('%H:%M:%S')
        self.log_text += f"[{timestamp}] {message}\n"
        self.log_display.text = self.log_text

    def connect_dog(self, instance):
        """连接机器狗"""
        if not SDK_AVAILABLE:
            self.add_log("错误: SDK 库未找到，请确保在支持的平台上运行")
            return

        if self.connected:
            self.add_log("已经连接到机器狗")
            return

        try:
            local_ip = self.local_ip_input.text
            dog_ip = self.dog_ip_input.text

            self.add_log(f"正在连接机器狗...")
            self.add_log(f"本地IP: {local_ip}, 机器狗IP: {dog_ip}")

            self.dog = mc_sdk_zsl_1_py.HighLevel()
            self.dog.initRobot(local_ip, 43988, dog_ip)

            self.connected = True
            self.connect_btn.text = '已连接'
            self.connect_btn.background_color = (0.3, 0.8, 0.3, 1)
            self.add_log("✓ 连接成功！")

        except Exception as e:
            self.add_log(f"✗ 连接失败: {str(e)}")
            self.connected = False

    def execute_command(self, command):
        """执行机器狗控制命令"""
        if not self.connected:
            self.add_log("请先连接机器狗")
            return

        try:
            self.add_log(f"执行命令: {command}")

            if command == 'standup':
                self.dog.standUp()
                time.sleep(3)
            elif command == 'liedown':
                self.dog.lieDown()
                time.sleep(3)
            elif command == 'forward':
                self.dog.move(0.2, 0, 0)
                time.sleep(2)
                self.dog.move(0, 0, 0)
            elif command == 'backward':
                self.dog.move(-0.2, 0, 0)
                time.sleep(2)
                self.dog.move(0, 0, 0)
            elif command == 'left':
                self.dog.move(0, 0.2, 0)
                time.sleep(2)
                self.dog.move(0, 0, 0)
            elif command == 'right':
                self.dog.move(0, -0.2, 0)
                time.sleep(2)
                self.dog.move(0, 0, 0)
            elif command == 'turn_left':
                self.dog.move(0, 0, 0.3)
                time.sleep(2)
                self.dog.move(0, 0, 0)
            elif command == 'turn_right':
                self.dog.move(0, 0, -0.3)
                time.sleep(2)
                self.dog.move(0, 0, 0)
            elif command == 'jump':
                self.dog.jump()
                time.sleep(4)
            elif command == 'front_jump':
                self.dog.frontJump()
                time.sleep(4)
            elif command == 'backflip':
                self.dog.backflip()
                time.sleep(4)
            elif command == 'shake_hand':
                self.dog.shakeHand()
                time.sleep(4)

            self.add_log(f"✓ 命令执行完成")

        except Exception as e:
            self.add_log(f"✗ 命令执行失败: {str(e)}")


if __name__ == '__main__':
    DogControlApp().run()
