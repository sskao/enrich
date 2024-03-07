class Enrich_Info(QGroupBox):
    def __init__(self, parent=None):
        super(Enrich_Info, self).__init__(parent)
        self.setTitle("Enrich")
        self.setGeometry(100, 100, 400, 200)       
        self.layout()
                   
    def layout(self):

        #-----------------------------------------
        filename='./userset/Enrich.txt'
        data_dict = {}
        # Open the text file for reading
        with open(filename, 'r') as file:
    
            for line in file:
                key, value = line.strip().split(':')
                key = key.strip()
                value = value.strip()
                data_dict[key] = value
        
        Valve1_Start=int(data_dict['Valve1_Start'])
        Valve1_Stop=int(data_dict['Valve1_Stop'])
        Valve2_Start=int(data_dict['Valve2_Start'])
        Valve2_Stop=int(data_dict['Valve2_Stop'])
        Heater_Start=int(data_dict['Heater_Start'])
        Heater_Stop=int(data_dict['Heater_Stop'])
        Fan_Start=int(data_dict['Fan_Start'])
        Fan_Stop=int(data_dict['Fan_Stop'])

        #-------------
        ScanTimes_Min=0
        ScanTimes_Max=500
        #-------------
        
        #----------------------------------------------
        self.Enrich2_label = QLabel("Valve1_5V/Start:")
        self.Enrich2_input = QSpinBox()
        self.Enrich2_input.setRange(ScanTimes_Min,ScanTimes_Max)
        self.Enrich2_input.setValue(Valve1_Start)
        #----------------------------------------------
        self.Enrich3_label = QLabel("Valve1_5V/Stop:")
        self.Enrich3_input = QSpinBox()
        self.Enrich3_input.setRange(ScanTimes_Min,ScanTimes_Max)
        self.Enrich3_input.setValue(Valve1_Stop)
        #----------------------------------------------
        self.Enrich4_label = QLabel("Valve2_5V/Start:")
        self.Enrich4_input = QSpinBox()
        self.Enrich4_input.setRange(ScanTimes_Min,ScanTimes_Max)
        self.Enrich4_input.setValue(Valve2_Start)
        #----------------------------------------------
        self.Enrich5_label = QLabel("Valve2_5V/Stop:")
        self.Enrich5_input = QSpinBox()
        self.Enrich5_input.setRange(ScanTimes_Min,ScanTimes_Max)
        self.Enrich5_input.setValue(Valve2_Stop)
        #----------------------------------------------
        self.Enrich6_label = QLabel("Heater_12V/Start:")
        self.Enrich6_input = QSpinBox()
        self.Enrich6_input.setRange(ScanTimes_Min,ScanTimes_Max)
        self.Enrich6_input.setValue(Heater_Start)
        #----------------------------------------------
        self.Enrich7_label = QLabel("Heater_12V/Stop:")
        self.Enrich7_input = QSpinBox()
        self.Enrich7_input.setRange(ScanTimes_Min,ScanTimes_Max)
        self.Enrich7_input.setValue(Heater_Stop)
        #-----------------------------------------

        #-----------------------------------------
        self.Enrich8_label = QLabel("Fan_24V/Start:")
        self.Enrich8_input = QSpinBox()
        self.Enrich8_input.setRange(ScanTimes_Min,ScanTimes_Max)
        self.Enrich8_input.setValue(Fan_Start)
        self.Enrich9_label = QLabel("Fan_24V/Stop:")
        self.Enrich9_input = QSpinBox()
        self.Enrich9_input.setRange(ScanTimes_Min,ScanTimes_Max)
        self.Enrich8_input.setValue(Fan_Stop)
        #-----------------------------------------
        
        self.save_button = QPushButton("Save")

        # Connect the button to the save function
        self.save_button.clicked.connect(self.save_data)

        # Set up the layout
        layout = QGridLayout()
        layout.addWidget(self.Enrich2_label,2,0,1,1)
        layout.addWidget(self.Enrich2_input,2,1,1,2)
        layout.addWidget(self.Enrich3_label,3,0,1,1)
        layout.addWidget(self.Enrich3_input,3,1,1,2)
        layout.addWidget(self.Enrich4_label,4,0,1,1)
        layout.addWidget(self.Enrich4_input,4,1,1,2)
        layout.addWidget(self.Enrich5_label,5,0,1,1)
        layout.addWidget(self.Enrich5_input,5,1,1,2)
        layout.addWidget(self.Enrich6_label,6,0,1,1)
        layout.addWidget(self.Enrich6_input,6,1,1,2)
        layout.addWidget(self.Enrich7_label,7,0,1,1)
        layout.addWidget(self.Enrich7_input,7,1,1,2)
        layout.addWidget(self.Enrich8_label,8,0,1,1)
        layout.addWidget(self.Enrich8_input,8,1,1,2)
        layout.addWidget(self.Enrich9_label,9,0,1,1)
        layout.addWidget(self.Enrich9_input,9,1,1,2)

        layout.addWidget(self.save_button,10,0,1,3)
        self.setLayout(layout)