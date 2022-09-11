from typing import List


class Translations:
    __slots__ = [
        "Language",
        "scenarioString",
        "label_Language",
        "pushButton_SaveScenario",
        "pushButton_AddScenario",
        "pushButton_DeleteScenario",
        "pushButton_start_multiple",
        "pushButton_Cancel",
        "page_borehole",
        "page_borehole_resistance",
        "pushButton_Results",
        "label_Status",
        "label_File",
        "label_Calculation",
        "label_Borehole_earth",
        "label_Earth_Properties",
        "checkBox_CalcDepth",
        "label_Settings",
        "label_H",
        "label_BS",
        "label_lambdaEarth",
        "label_GroundTemp",
        "label_BoreholeResistance",
        "label_WidthField",
        "label_LengthField",
        "label_TempConstraints",
        "label_TempMin",
        "label_TempMax",
        "label_SimulationTime",
        "pushButton_NextGeneral",
        "pushButton_PreviousThermal",
        "label_Size",
        "checkBox_Legend",
        "pushButton_SaveData",
        "pushButton_SaveFigure",
        "X_Axis",
        "Y_Axis",
        "BaseCooling",
        "BaseHeating",
        "PeakCooling",
        "PeakHeating",
        "label_ThermalDemandsTitle",
        "label_Import",
        "checkBox_Import",
        "label_ThermalDemands",
        "label_pH",
        "label_pC",
        "label_HL",
        "label_CL",
        "label_UnitPeak",
        "label_UnitLoad",
        "label_Jan",
        "label_Feb",
        "label_Mar",
        "label_Apr",
        "label_May",
        "label_Jun",
        "label_Jul",
        "label_Aug",
        "label_Sep",
        "label_Oct",
        "label_Nov",
        "label_Dec",
        "label_DataType",
        "label_Filename",
        "label_SheetName",
        "pushButton_load",
        "toolBoxFile",
        "toolBoxDataLocation",
        "label_dataColumn",
        "label_DataUnit",
        "label_HeatingLoadLine",
        "label_CoolingLoadLine",
        "label_combined",
        "label_TimeStep",
        "label_DateLine",
        "comboBoxDataColumnList",
        "comboBoxTimeStepList",
        "pushButton_calculate",
        "ErrorMassage",
        "UnableDataFormat",
        "ChooseCSV",
        "ChooseXLS",
        "ChooseXLSX",
        "NoFileSelected",
        "ValueError",
        "ColumnError",
        "ChoosePKL",
        "SaveFigure",
        "SaveData",
        "SavePKL",
        "label_WarningCustomBorefield",
        "label_WarningDepth",
        "checkBox_SizeBorefield",
        "label_H_max",
        "label_B_min",
        "label_B_max",
        "label_MaxWidthField",
        "label_MaxLengthField",
        "label_Size_B",
        "label_Size_L",
        "label_Size_W",
        "comboBoxSizeMethodList",
        "label_German",
        "label_English",
        "label_New",
        "label_Save",
        "label_Open",
        "label_Save_As",
        "Calculation_Finished",
        "GHE_tool_imported",
        "GHE_tool_imported_start",
        "label_Dutch",
        "label_Italian",
        "label_French",
        "comboBoxLanguageList",
        "label_new_scenario",
        "new_name",
        "label_okay",
        "label_abort",
        "NoBackupFile",
        "pushButton_borehole_resistance",
        "label_Spanish",
        "label_Galician",
        "label_close",
        "label_cancel",
        "label_CancelTitle",
        "label_LeaveScenarioText",
        "label_LeaveScenario",
        "label_StayScenario",
        "X_Axis_Load",
        "Y_Axis_Load_P",
        "Y_Axis_Load_Q",
        "label_aim",
        "menuLanguage",
        "menuSettings",
        "menuCalculation",
        "menuFile",
        "menuScenario",
        "action_start_multiple",
        "actionGerman",
        "actionEnglish",
        "actionDutch",
        "actionFrench",
        "actionItalian",
        "actionNew",
        "actionSave",
        "actionOpen",
        "actionUpdate_Scenario",
        "actionAdd_Scenario",
        "actionDelete_scenario",
        "actionSave_As",
        "actionRename_scenario",
        "button_rename_scenario",
        "label_Language_Head",
        "label_aim_question",
        "pushButton_PreviousResistance",
        "pushButton_NextResistance",
        "comboBox_AimList",
        "label_Seperator",
        "label_SeperatorDataFile",
        "comboBox_SeperatorList",
        "label_data_file",
        "label_Filename_2",
        "label_dataColumn_2",
        "label_HeatingLoadLine_2",
        "label_CoolingLoadLine_2",
        "label_combined_2",
        "label_DataUnit_2",
        "label_Scenario_Head",
        "checkBox_AutoSaving",
        "label_Scenario_Hint",
        "label_Borehole_Resistance",
        "label_Borehole_Resistance_Head",
        "label_Rb_calculation_method",
        "comboBox_Rb_methodList",
        "label_fluid_data",
        "label_fluid_lambda",
        "label_fluid_mass_flow_rate",
        "label_fluid_density",
        "label_fluid_thermal_capacity",
        "label_fluid_viscosity",
        "label_pipe_data",
        "label_NumberOfPipes",
        "label_grout_conductivity",
        "label_pipe_conductivity",
        "label_pipe_outer_radius",
        "label_pipe_inner_radius",
        "label_borehole_radius",
        "label_pipe_distance",
        "label_pipe_roughness",
        "label_borehole_burial_depth",
        "label_ResOptimizeLoad1",
        "label_ResOptimizeLoad2",
        "label_ResOptimizeLoad3",
        "label_ResOptimizeLoad4",
        "label_CancelText",
        "label_ResOptimizeLoad5",
        "label_ResOptimizeLoad6",
        "pushButton_start_single",
        "NotCalculated",
        "NoSolution",
        "comboBox_decimalList",
        "label_decimalDataFile",
        "label_decimal",
        "actionSpanish",
        "actionGalician",
        "option_language",
    ]

    def __init__(self):
        self.option_language: List[str] = ["English", "German", "Dutch", "Italian", "French", "Spanish", "Galician"]
        self.Language: List[str] = ["0", "1", "2", "3", "4", "5", "6"]
        self.scenarioString: List[str] = ["Scenario", "Szenario", "Scenario", "Scenario", "Scénario", "Escenario", "Escenario"]
        self.label_Language: List[str] = ["Language: ", "Sprache: ", "Taal: ", "Languange: ", "Languange: ", "Idioma:", "Lingua: "]
        self.pushButton_SaveScenario: List[str] = [
            "Update scenario",
            "Szenario aktualisieren",
            "Update scenario",
            "Aggiorna scenario",
            "Mettre à jour le scénario",
            "Actualizar escenario",
            "Actualizar escenario",
        ]
        self.pushButton_AddScenario: List[str] = [
            "Add scenario",
            "Szenario hinzufügen",
            "Nieuw scenario",
            "Aggiungi scenario",
            "Ajouter un scénario",
            "Añadir escenario",
            "Engadir escenario",
        ]
        self.pushButton_DeleteScenario: List[str] = [
            "Delete scenario",
            "Szenario löschen",
            "Verwijder scenario",
            "Cancella scenario",
            "Supprimer un scénario",
            "Borrar escenario",
            "Eliminar escenario",
        ]
        self.pushButton_start_multiple: List[str] = [
            "Calculate all scenarios",
            "Berechne alle Szenarios",
            "Bereken alle scenarios",
            "Calculate all scenarios",
            "Calculate all scenarios",
            "Calculate all scenarios",
            "Calculate all scenarios",
        ]
        self.pushButton_Cancel: List[str] = ["Exit", "Verlassen", "Sluit", "Esci", "Sortie", "Salir", "Saír"]
        self.page_borehole: List[str] = [
            "Borehole \\nand earth",
            "Bohrloch \\nund Erdreich",
            "Boorveld \\n en grond",
            "Foro e \\nterra",
            "Forage \\net terre",
            "Pozo \\ny terreno",
            "Pozo \\ne chan",
        ]
        self.page_borehole_resistance: List[str] = [
            "Thermal \\ndemands",
            "Thermischer \\nBedarf",
            "Thermische \\nvraag",
            "Richieste \\ntermiche",
            "Demande \\nthermique",
            "Cargas \\ntérmicas",
            "Cargas \\ntérmicas",
        ]
        self.pushButton_Results: List[str] = ["Results", "Ergebnisse", "Resultaten", "Risultati", "Résultats", "Resultados", "Resultados"]
        self.label_Status: List[str] = ["Progress: ", "Fortschritt: ", "Vooruitgang: ", "Progressi: ", "Progrès: ", "Progreso: ", "Progreso: "]
        self.label_File: List[str] = ["File", "Datei", "Bestand", "File", "File", "File", "File"]
        self.label_Calculation: List[str] = ["Calculation", "Berechnung", "Berekening", "Calculation", "Calculation", "Calculation", "Calculation"]
        self.label_Borehole_earth: List[str] = [
            "Borehole and earth",
            "Bohrloch und Erdreich",
            "Boorveld en grond",
            "Foro e terra",
            "Forage et terre",
            "Pozo y terreno",
            "Pozo e chan",
        ]
        self.label_Earth_Properties: List[str] = [
            "Borehole and earth properties",
            "Bohrloch und Erdreicheigenschaften",
            "Eigenschappen van boorveld en grond",
            "Proprietà del foro e della terra",
            "Propriétés du trou de sonde et de la terre",
            "Propiedades del pozo y terreno",
            "Propiedades do pozo e do chan",
        ]
        self.checkBox_CalcDepth: List[str] = [
            "Determine the required depth",
            "Notwendige Bohrlochlänge bestimmen",
            "Bepaal de benodigde diepte",
            "Determinare la profondità richiesta",
            "Déterminer la profondeur requise",
            "Determinar la longitud requerida",
            "Determinar a lonxitude necesaria",
        ]
        self.label_Settings: List[str] = ["Settings", "Einstellungen", "Instellingen", "Settings", "Settings", "Settings", "Settings"]
        self.label_H: List[str] = [
            "Borehole depth [m]: ",
            "Bohrlochtiefe [m]: ",
            "Boorgatdiepte [m]: ",
            "Profondità foro [m]: ",
            "Profondeur du forage [m]: ",
            "Profundidad del pozo [m]: ",
            "Profundidade do pozo [m]: ",
        ]
        self.label_BS: List[str] = [
            "Borehole spacing [m]: ",
            "Bohrlochabstand [m]: ",
            "Boorgatspatiring [m]: ",
            "Spaziatura del foro [m]: ",
            "Espacement des trous de forage [m]: ",
            "Espaciado entre pozos [m]: ",
            "Espazamento entre pozos [m]: ",
        ]
        self.label_lambdaEarth: List[str] = [
            "Conductivity of the soil [W/mK]: ",
            "Wärmeleitfähigkeit des Erdreiches [W/mK]: ",
            "Conductiviteit van de bodem [W/mK]: ",
            "Conducibilità del terreno [W/mK]: ",
            "Conductivité du sol [W/mK]: ",
            "Conductividad del suelo [W/mK]: ",
            "Conductividade do chan [W/mK]: ",
        ]
        self.label_GroundTemp: List[str] = [
            "Ground temperature at infinity [°C]: ",
            "Erdreichtemperatur in der Unendlichkeit [°C]: ",
            "Grondtemperatuur op oneindig [°C]: ",
            "Temperatura del terreno all'infinito [°C]: ",
            "Température du sol à l'infini [°C]: ",
            "Temperatura del suelo en el infinito [°C]: ",
            "Temperatura do chan no infinito [°C]: ",
        ]
        self.label_BoreholeResistance: List[str] = [
            "Equivalent borehole resistance [mK/W]: ",
            "Äquivalenter Bohrlochwiderstand [mK/W]: ",
            "Equivalente boorgatweerstand [mK/W]: ",
            "Resistenza equivalente del foro [mK/W]: ",
            "Résistance équivalente du trou de forage [mK/W]: ",
            "Resistencia del pozo equivalente [mK/W]: ",
            "Resistencia do pozo equivalente [mK/W]: ",
        ]
        self.label_WidthField: List[str] = [
            "Width of rectangular field [#]: ",
            "Breite des rechteckigen Feldes [#]: ",
            "Breedte van het rechthoekige veld [#]: ",
            "Larghezza del campo rettangolare [#]: ",
            "Largeur du champ rectangulaire [#]: ",
            "Ancho del campo rectangular [#]: ",
            "Ancho do campo rectangular [#]: ",
        ]
        self.label_LengthField: List[str] = [
            "Length of rectangular field [#]: ",
            "Länge des rechteckigen Feldes [#]: ",
            "Lengte van het rechthoekige veld [#]: ",
            "Lunghezza del campo rettangolare [#]: ",
            "Longueur du champ rectangulaire [#]: ",
            "Longitud del campo rectangular [#]: ",
            "Lonxitude do campo rectangular [#]: ",
        ]
        self.label_TempConstraints: List[str] = [
            "Temperature constraints and simulation period",
            "Temperaturgrenzwerte und Simulationszeit",
            "Temperatuursgrenzen en simulatieperiode",
            "Vincoli di temperatura e periodo di simulazione",
            "Contraintes de température et période de simulation",
            "Restricciones de temperatura y período de simulación",
            "Restriccións de temperatura e período de simulación",
        ]
        self.label_TempMin: List[str] = [
            "Minimal temperature [°C]: ",
            "Minimaltemperatur [°C]: ",
            "Minimale temperatuur [°C]: ",
            "Temperatura minima [°C]: ",
            "Température minimale [°C]: ",
            "Temperatura mínima [°C]: ",
            "Temperatura mínima[°C]: ",
        ]
        self.label_TempMax: List[str] = [
            "Maximal temperature [°C]: ",
            "Maximaltemperatur [°C]: ",
            "Maximale temperatuur [°C]: ",
            "Temperatura massima [°C]: ",
            "Température maximale [°C]: ",
            "Temperatura máxima [°C]: ",
            "Temperatura máxima [°C]: ",
        ]
        self.label_SimulationTime: List[str] = [
            "Simulation period [yrs]: ",
            "Simulationszeit [Jahre]: ",
            "Simulatieperiode [jaar]: ",
            "Periodo di simulazione [anni]: ",
            "Période de simulation [années]: ",
            "Período de simulación [años]: ",
            "Período de simulación [anos]: ",
        ]
        self.pushButton_NextGeneral: List[str] = ["  next  ", "  nächstes  ", "  volgende  ", "  successivo  ", "  suivant  ", "  siguiente  ", "  seguinte  "]
        self.pushButton_PreviousThermal: List[str] = [
            "  previous  ",
            "  vorheriges  ",
            "  vorige  ",
            "  precedente  ",
            "  précédente  ",
            "  anterior  ",
            "  anterior  ",
        ]
        self.label_Size: List[str] = [
            "Borehole depth: ",
            "Bohrlochtiefe: ",
            "Boorgatdiepte: ",
            "Profondità del foro:  ",
            "Profondeur du trou de sonde: ",
            "Profundidad del pozo: ",
            "Profundidade do pozo: ",
        ]
        self.checkBox_Legend: List[str] = [
            "Show legend?",
            "Legende zeigen?",
            "Toon legende?",
            "Mostra la legenda?",
            "Afficher la légende?",
            "Mostrar leyenda?",
            "Mostrar lenda?",
        ]
        self.pushButton_SaveData: List[str] = [
            "Save results",
            "Ergebnisse speichern",
            "Bewaar resultaten",
            "Salva i risultati",
            "Enregistrer les résultats",
            "Guardar resultados",
            "Gardar resultados",
        ]
        self.pushButton_SaveFigure: List[str] = [
            "Save figure",
            "Abbildung speichern",
            "Bewaar figuren",
            "Salva figura",
            "Sauvegarder la figure",
            "Guardar figura",
            "Gardar figura",
        ]
        self.X_Axis: List[str] = ["Time [year]", "Zeit [Jahr]", "Tijd [jaar]", "Tempo [anno]", "Heure [année]", "Tiempo [año]", "Tempo [ano]"]
        self.Y_Axis: List[str] = [
            "Temperature [°C]",
            "Temperatur [°C]",
            "Temperatuur [°C]",
            "Temperatura [°C]",
            "Température [°C]",
            "Temperatura [°C]",
            "Temperatura [°C]",
        ]
        self.BaseCooling: List[str] = [
            "base cooling",
            "Grundkühlung",
            "basisbelasting koeling",
            "Base raffreddamento",
            "Base de refroidissement",
            "Base de refrigeración",
            "Base de refrixeración",
        ]
        self.BaseHeating: List[str] = [
            "base heating",
            "Grundheizung",
            "basisbelasting verwarming",
            "Base riscaldamento",
            "Chauffage de base",
            "Base de calefacción",
            "Base de calefacción",
        ]
        self.PeakCooling: List[str] = [
            "peak cooling",
            "Kühlspitzen",
            "piekkoeling",
            "Picco raffreddamento",
            "Refroidissement maximal",
            "Pico de refrigeración",
            "Pico de refrixeración",
        ]
        self.PeakHeating: List[str] = [
            "peak heating",
            "Heizspitzen",
            "piekverwarming",
            "Picco di riscaldamento",
            "Pic de chauffage",
            "Pico de calefacción",
            "Pico de calefacción",
        ]
        self.label_ThermalDemandsTitle: List[str] = [
            "Thermal demands",
            "Thermische Last",
            "Thermische vraag",
            "Richieste termiche",
            "Demande thermique",
            "Cargas térmicas",
            "Cargas térmicas",
        ]
        self.label_Import: List[str] = ["Import", "Importieren", "Importeer", "Importazione", "Importation", "Importar", "Importar"]
        self.checkBox_Import: List[str] = [
            "Import Demands?",
            "Lasten importieren?",
            "Importeer vraag?",
            "Richieste di \\nimportazione?",
            "Demande d'importation?",
            "Importar cargas?",
            "Importar cargas?",
        ]
        self.label_ThermalDemands: List[str] = [
            "Thermal demands",
            "Thermische Last",
            "Thermische vraag",
            "Richieste termiche",
            "Demande thermique",
            "Cargas térmicas",
            "Cargas térmicas",
        ]
        self.label_pH: List[str] = [
            "Heating peak",
            "Heizspitzen",
            "Verwarmingspiek",
            "Picco di riscaldamento",
            "Pic de chauffage",
            "Pico de calefacción",
            "Pico de calefacción",
        ]
        self.label_pC: List[str] = [
            "Cooling peak",
            "Kühlspitzen",
            "Koelpiek",
            "Picco di raffreddamento",
            "Pic de refroidissement",
            "Pico de refrigeración",
            "Pico de refrixeración",
        ]
        self.label_HL: List[str] = [
            "Heating load",
            "Heizlast",
            "Belasting verwarming",
            "Carico di riscaldamento",
            "Charge de chauffage",
            "Carga de calefacción",
            "Carga de calefacción",
        ]
        self.label_CL: List[str] = [
            "Cooling load",
            "Kühllast",
            "Belasting koeling",
            "Carico di raffreddamento",
            "Charge de refroidissement",
            "Carga de refrigeración",
            "Carga de refrixeración",
        ]
        self.label_UnitPeak: List[str] = [
            "Peak unit: ",
            "Einheit Spitze: ",
            "Eenheid piek: ",
            "Unità di picco: ",
            "Unité de pointe: ",
            "Unidad de pico: ",
            "Unidade de pico: ",
        ]
        self.label_UnitLoad: List[str] = [
            "Load unit: ",
            "Einheit Last: ",
            "Eenheid belasting: ",
            "Unità di carico: ",
            "Unité de charge: ",
            "Unidad de carga: ",
            "Unidade de carga: ",
        ]
        self.label_Jan: List[str] = ["January", "Januar", "Januari", "Gennaio", "Janvier", "Enero", "Xaneiro"]
        self.label_Feb: List[str] = ["February", "Februar", "Februari", "Febbraio", "Février", "Febrero", "Febreiro"]
        self.label_Mar: List[str] = ["March", "März", "Maart", "Marzo", "Mars", "Marzo", "Marzo"]
        self.label_Apr: List[str] = ["April", "April", "April", "Aprile", "Avril", "Abril", "Abril"]
        self.label_May: List[str] = ["May", "Mai", "Mei", "Maggio", "Mai", "Mayo", "Maio"]
        self.label_Jun: List[str] = ["June", "Juni", "Juni", "Giugno", "Juin", "Junio", "Xuño"]
        self.label_Jul: List[str] = ["July", "Juli", "Juli", "Luglio", "Juillet", "Julio", "Xullo"]
        self.label_Aug: List[str] = ["August", "August", "Augustus", "Agosto", "Août", "Agosto", "Agosto"]
        self.label_Sep: List[str] = ["September", "September", "September", "Settembre", "Septembre", "Septiembre", "Setembro"]
        self.label_Oct: List[str] = ["October", "Oktober", "Oktober", "Ottobre", "Octobre", "Octubre", "Outubro"]
        self.label_Nov: List[str] = ["November", "November", "November", "Novembre", "Novembre", "Noviembre", "Novembro"]
        self.label_Dec: List[str] = ["December", "Dezember", "December", "Dicembre", "Décembre", "Diciembre", "Decembro"]
        self.label_DataType: List[str] = [
            "File type: ",
            "Dateityp: ",
            "Bestandstype: ",
            "Tipo di fileImport: ",
            "Type de fichier: ",
            "Tipo de archivo: ",
            "Tipo de ficheiro: ",
        ]
        self.label_Filename: List[str] = [
            "Filename: ",
            "Dateiname: ",
            "Bestandsnaam: ",
            "Nome fileImport: ",
            "Nom de fichier: ",
            "Nombre de archivo: ",
            "Nome de ficheiro: ",
        ]
        self.label_SheetName: List[str] = [
            "Sheet name: ",
            "Tabellenblattname: ",
            "Naam van het blad: ",
            "Nome foglio:  ",
            "Nom de la feuille: ",
            "Nombre de hoja: ",
            "Nome de folla: ",
        ]
        self.pushButton_load: List[str] = ["Load", "Laden", "Laad", "Caricare", "Chargement", "Cargar", "Cargar"]
        self.toolBoxFile: List[str] = [
            "Data fileImport",
            "Datendatei",
            "Databestand",
            "File dati",
            "Fichier de données",
            "Fichier de données",
            "Fichier de données",
        ]
        self.toolBoxDataLocation: List[str] = [
            "Data location in fileImport",
            "Speicherort der Daten in der Datei",
            "Locatie van de data in bestand",
            "Posizione dati nel fileImport",
            "Emplacement des données dans le fichier",
            "Data location in fileImport",
            "Data location in fileImport",
        ]
        self.label_dataColumn: List[str] = [
            "Thermal demands: ",
            "Thermische Lasten: ",
            "Thermische vraag: ",
            "Richieste termiche: ",
            "Demande thermique: ",
            "Cargas térmicas: ",
            "Cargas térmicas: ",
        ]
        self.label_DataUnit: List[str] = [
            "Unit data: ",
            "Dateneinheit: ",
            "Eenheid data: ",
            "Dati \\ndell'unità:  ",
            "Données de l'unité: ",
            "Datos de unidad: ",
            "Datos de unidade: ",
        ]
        self.label_HeatingLoadLine: List[str] = [
            "Heating load line: ",
            "Heizlastspalte: ",
            "Belastingslijn verwarming: ",
            "Linea di carico di riscaldamento: ",
            "Ligne de charge de chauffage: ",
            "Línea de carga de calefacción: ",
            "Liña de carga de calefacción: ",
        ]
        self.label_CoolingLoadLine: List[str] = [
            "Cooling load line: ",
            "Kühllastspalte: ",
            "Belastingslijn koeling: ",
            "Linea del carico di raffreddamento: ",
            "Ligne de charge de refroidissement: ",
            "Línea de carga de refrigeración: ",
            "Liña de carga de refrixeración: ",
        ]
        self.label_combined: List[str] = [
            "Load line: ",
            "Load line: ",
            "Belastingslijn: ",
            "Linea di carico: ",
            "Ligne de charge: ",
            "Línea de carga: ",
            "Liña de carga: ",
        ]
        self.label_TimeStep: List[str] = [
            "Time step: ",
            "Zeitschritt: ",
            "Tijdsstap: ",
            "Passo temporale: ",
            "Pas de temps: ",
            "Paso temporal: ",
            "Paso temporal: ",
        ]
        self.label_DateLine: List[str] = [
            "Date line: ",
            "Datumsspalte: ",
            "Datumlijn: ",
            "Linea della data: ",
            "Ligne de date: ",
            "Línea de fecha: ",
            "Liña de data: ",
        ]
        self.comboBoxDataColumnList: List[str] = [
            "['2 columns', '1 column']",
            "['2 Spalten', '1 Spalte']",
            "['2 kolommen', '1 kolom']",
            "['2 colonne', '1 colonna']",
            "['2 colonnes', '1 colonne']",
            "['2 columnas', '1 columna']",
            "['2 columnas', '1 columna']",
        ]
        self.comboBoxTimeStepList: List[str] = [
            "['1 hr.', '15 Min.', 'Automatic']",
            "['1 Std.', '15 Min.', 'Automatisch']",
            "['1 uur', '15 min.', 'Automatisch']",
            "['1 Ora', '15 Min.', 'Automatico']",
            "['1 Std.', '15 Min.', 'Automatique']",
            "['1 hr.', '15 Min.', 'Automático']",
            "['1 hr.', '15 Min.', 'Automático']",
        ]
        self.pushButton_calculate: List[str] = ["Calculate", "Berechne", "Bereken", "Calcola", "Calculer", "Calcular", "Calcular"]
        self.ErrorMassage: List[str] = ["Error!", "Fehler!", "Error!", "Errore!", "Erreur!", "Error!", "Erro!"]
        self.UnableDataFormat: List[str] = [
            "Unable to open selected data format!",
            "Das ausgewählte Datenformat kann nicht geöffnet werden!",
            "Het is niet mogelijk het geselecteerde dataformaat te openen!",
            "Impossibile aprire il formato dati selezionato!",
            "Impossible d'ouvrir le format de données sélectionné!",
            "No se puede abrir el formato de datos seleccionado!",
            "Non se pode abrir o formato de datos escollido!",
        ]
        self.ChooseCSV: List[str] = [
            "Choose csv to load data fileImport",
            "Wählen Sie csv zum Laden einer Datendatei",
            "Selecteer csv",
            "Scegli csv per caricare il fileImport dei dati",
            "Choisissez csv pour charger le fichier de données.",
            "Elija csv para cargar el archivo de datos",
            "Escolla csv para cargar o ficheiro de datos",
        ]
        self.ChooseXLS: List[str] = [
            "Choose xlsx to load data fileImport",
            "Wählen Sie xlsx zum Laden einer Datendatei",
            "Selecteer xlsx",
            "Scegli xlsx per caricare il fileImport di dati",
            "Choisissez xlsx pour charger le fichier de données",
            "Elija xlsx para cargar el archivo de datos",
            "Escolla xlsx para cargar o ficheiro de datos",
        ]
        self.ChooseXLSX: List[str] = [
            "Choose xls to load data fileImport",
            "Wählen Sie xls zum Laden einer Datendatei",
            "Selecteer xls",
            "Scegli xls per caricare il fileImport di dati",
            "Choisissez xls pour charger le fichier de données",
            "Elija xls para cargar el archivo de datos",
            "Escolla xls para cargar o ficheiro de datos",
        ]
        self.NoFileSelected: List[str] = [
            "No file selected.",
            "Keine Datei ausgewählt.",
            "Geen bestand geselecteerd.",
            "Nessun il file selezionato.",
            "Aucun fichier sélectionné.",
            "No se ha seleccionado ningún archivo.",
            "Non se escolleu ningún ficheiro.",
        ]
        self.ValueError: List[str] = [
            "Value error: check selected columns",
            "Wertefehler: ausgewählte Spalten prüfen",
            "Value error: controleer geselecteerde kolommen",
            "Errore di valore: controlla le colonne selezionate",
            "Erreur de valeur : vérifiez les colonnes sélectionnées",
            "Error de valor: compruebe las columnas seleccionadas",
            "Erro de valor: comprobe as columnas escollidas",
        ]
        self.ColumnError: List[str] = [
            "Wrong column: check selected columns",
            "Falsche Spalte: ausgewählte Spalten prüfen",
            "Wrong column: controleer geselecteerde kolommen",
            "Colonna errata: controlla le colonne selezionate",
            "Colonne incorrecte : vérifiez les colonnes sélectionnées",
            "Columna incorrecta: compruebe las columnas seleccionadas",
            "Columna incorrecta: comprobe as columnas escollidas",
        ]
        self.ChoosePKL: List[str] = [
            "Choose pkl to load scenarios",
            "Wählen Sie pkl zum Laden von Szenarien",
            "Kies pkl bestand",
            "Scegliere pkl per caricare gli scenari",
            "Choisir pkl pour charger les scénarios",
            "Elija pkl para cargar escenarios",
            "Escolla pkl para cargar escenarios",
        ]
        self.SaveFigure: List[str] = [
            "Choose png location to save figure",
            "Wählen Sie einen png-Speicherort für die Abbildung",
            "Kies gewenste png locatie",
            "Scegli il percorso png per salvare la figura",
            "Choisissez l'emplacement png pour enregistrer la figure",
            "Elija la localización del png para guardar figura",
            "Escolla a localización do png para gardar figura",
        ]
        self.SaveData: List[str] = [
            "Choose csv location to save results",
            "Wählen Sie einen csv-Speicherort zum Speichern der Ergebnisse",
            "Kies gewenste csv locatie",
            "Scegli il percorso csv per salvare i risultati",
            "Choisissez l'emplacement csv pour enregistrer les résultats",
            "Elija la localización del csv para guardar resultados",
            "Escolla a localización do csv para gardar resultados",
        ]
        self.SavePKL: List[str] = [
            "Choose pkl location to save scenarios",
            "Wählen Sie den pkl-Speicherort zum Speichern von Szenarien",
            "Kies gewenste pkl locatie",
            "Scegli il percorso pkl per salvare gli scenari",
            "Choisissez un emplacement pkl pour enregistrer les scénarios",
            "Elija la localización del pkl para guardar escenarios",
            "Escolla a localización do pkl para gardar escenarios",
        ]
        self.label_WarningCustomBorefield: List[str] = [
            "With the selected values a customized bore field will be calculated. This will dramatically increase the calculation time.",
            "Mit den gewählten Werten wird ein individuelles Borefeld berechnet. Dadurch wird die Berechnungszeit drastisch erhöht.",
            "Met de geselecteerde waarden moet een aangepast boorveld worden berekend.Dit zal de berekentijd drastisch doen toenemen.",
            "With the selected values a customized bore field will be calculated. This will dramatically increase the calculation time.",
            "With the selected values a customized bore field will be calculated. This will dramatically increase the calculation time.",
            "Un campo de captación será calculado con los valores seleccionados. El tiempo de computación aumentará drásticamente.",
            "Calcularase un campo de captación cos valores escollidos. O tempo de cálculo aumentará drásticamente.",
        ]
        self.label_WarningDepth: List[str] = [
            "The calculated size is below the suggested minimum of 50 m. The calculation may be incorrect.",
            "Die berechnete Größe liegt unter dem empfohlenen Minimum von 50 m. Die Berechnung ist möglicherweise fehlerhaft.",
            "De berekende diepte is lager dan het voorgestelde minimum van 50m.De berekening kan inaccuraat zijn.",
            "The calculated size is below the suggested minimum of 50 m. The calculation may be incorrect.",
            "The calculated size is below the suggested minimum of 50 m. The calculation may be incorrect.",
            "El tamaño calculado se encuentra por debajo del mínimo sugerido de 15 m. El dimensionado puede no ser correcto.",
            "O tamaño calculado está por debaixo do mínimo suxerido de 15 m. O dimensionado pode non ser o correcto.",
        ]
        self.checkBox_SizeBorefield: List[str] = [
            "Size borefield by length and width",
            "Dimensionierung des Bohrlochfeldes nach Länge und Breite",
            "Dimensioneer boorveld met breedte en lengte",
            "Size borefield by length and width",
            "Size borefield by length and width",
            "Size borefield by length and width",
            "Size borefield by length and width",
        ]
        self.label_H_max: List[str] = [
            "Maximal borehole depth [m]: ",
            "Maximale Bohrlochtiefe [m]: ",
            "Maximale boorvelddiepte[m]: ",
            "Maximal borehole depth [m]: ",
            "Maximal borehole depth [m]: ",
            "Maximal borehole depth [m]: ",
            "Maximal borehole depth [m]: ",
        ]
        self.label_B_min: List[str] = [
            "Minimal borehole spacing [m]: ",
            "Minimaler Bohrlochabstand [m]: ",
            "Minimale boorgatspatiëring [m]: ",
            "Minimal borehole spacing [m]: ",
            "Minimal borehole spacing [m]: ",
            "Minimal borehole spacing [m]: ",
            "Minimal borehole spacing [m]: ",
        ]
        self.label_B_max: List[str] = [
            "Maximal borehole spacing [m]: ",
            "Maximaler Bohrlochabstand [m]: ",
            "Maximale boorgatspatiëring [m]: ",
            "Maximal borehole spacing [m]: ",
            "Maximal borehole spacing [m]: ",
            "Maximal borehole spacing [m]: ",
            "Maximal borehole spacing [m]: ",
        ]
        self.label_MaxWidthField: List[str] = [
            "Maximal width of rectangular field [m]: ",
            "Maximale Breite des rechteckigen Feldes [m]: ",
            "Maximale breedte van het rechthoekig boorveld [m]: ",
            "Maximal width of rectangular field [m]: ",
            "Maximal width of rectangular field [m]: ",
            "Maximal width of rectangular field [m]: ",
            "Maximal width of rectangular field [m]: ",
        ]
        self.label_MaxLengthField: List[str] = [
            "Maximal length of rectangular field [m]: ",
            "Maximale Länge des rechteckigen Feldes [m]: ",
            "Maximale lengte van het rechthoekig boorveld [m]: ",
            "Maximal length of rectangular field [m]: ",
            "Maximal length of rectangular field [m]: ",
            "Maximal length of rectangular field [m]: ",
            "Maximal length of rectangular field [m]: ",
        ]
        self.label_Size_B: List[str] = [
            "Borehole spacing: ",
            "Bohrlochabstand: ",
            "Boorgatspatiëring: ",
            "Borehole spacing: ",
            "Borehole spacing: ",
            "Borehole spacing: ",
            "Borehole spacing: ",
        ]
        self.label_Size_L: List[str] = [
            "Length of rectangular field: ",
            "Länge des rechteckigen Feldes: ",
            "Lengte van het rechthoekig veld: ",
            "Length of rectangular field: ",
            "Length of rectangular field: ",
            "Length of rectangular field: ",
            "Length of rectangular field: ",
        ]
        self.label_Size_W: List[str] = [
            "Width of rectangular field: ",
            "Breite des rechteckigen Feldes: ",
            "Breedte van het rechthoekig veld: ",
            "Width of rectangular field: ",
            "Width of rectangular field: ",
            "Width of rectangular field: ",
            "Width of rectangular field: ",
        ]
        self.comboBoxSizeMethodList: List[str] = [
            "['Fast', 'Robust']",
            "['Schnell', 'Robust']",
            "['Snel', 'Robuust']",
            "['Fast', 'Robust']",
            "['Fast', 'Robust']",
            "['Fast', 'Robust']",
            "['Fast', 'Robust']",
        ]
        self.label_German: List[str] = ["German", "Deutsch", "Duits", "German", "German", "German", "German"]
        self.label_English: List[str] = ["English", "Englisch", "Engels", "English", "English", "English", "English"]
        self.label_New: List[str] = ["New Project", "Neues Projekt", "Nieuw project", "New Project", "New Project", "New Project", "New Project"]
        self.label_Save: List[str] = ["Save Project", "Speichere Projekt", "Bewaar project", "Save Project", "Save Project", "Save Project", "Save Project"]
        self.label_Open: List[str] = ["Open Project", "Öffne Projekt", "Open project", "Open Project", "Open Project", "Open Project", "Open Project"]
        self.label_Save_As: List[str] = ["Save as", "Speichere Projekt unter ...", "Sla op als", "Save as", "Save as", "Save as", "Save as"]
        self.Calculation_Finished: List[str] = [
            "Calculation finished",
            "Berechnung fertiggestellt",
            "Berekening beëindigd",
            "Calculation finished",
            "Calculation finished",
            "Calculation finished",
            "Calculation finished",
        ]
        self.GHE_tool_imported: List[str] = [
            "GHEtool imported",
            "GHEtool importiert",
            "GHEtool geïmporteerd",
            "GHEtool imported",
            "GHEtool imported",
            "GHEtool imported",
            "GHEtool imported",
        ]
        self.GHE_tool_imported_start: List[str] = [
            "Start importing GHEtool",
            "Starte GHEtool zu importieren",
            "Start importering GHEtool",
            "Start importing GHEtool",
            "Start importing GHEtool",
            "Start importing GHEtool",
            "Start importing GHEtool",
        ]
        self.label_Dutch: List[str] = ["Dutch", "Niederländisch", "Nederlands", "Dutch", "Dutch", "Dutch", "Dutch"]
        self.label_Italian: List[str] = ["Italian", "Italienisch", "Italiaans", "Italian", "Italian", "Italian", "Italian"]
        self.label_French: List[str] = ["French", "Französisch", "Frans", "French", "French", "French", "French"]
        self.comboBoxLanguageList: List[str] = [
            "['English', 'German', 'Dutch', 'Italian', 'French', 'Spanish', 'Galician']",
            "['Englisch', 'Deutsch', 'Niederländisch', 'Italienisch', 'Französisch', 'Spanisch', 'Galizisch']",
            "['Engels', 'Duits', 'Nederlands', 'Italiaans', 'Frans', 'Spaans', 'Galisisch']",
            "['English', 'German', 'Dutch', 'Italian', 'French', 'Spanish', 'Galician']",
            "['English', 'German', 'Dutch', 'Italian', 'French', 'Spanish', 'Galician']",
            "['English', 'German', 'Dutch', 'Italian', 'French', 'Spanish', 'Galician']",
            "['English', 'German', 'Dutch', 'Italian', 'French', 'Spanish', 'Galician']",
        ]
        self.label_new_scenario: List[str] = [
            "Enter new scenario name",
            "Neuer Name für das Szenario",
            "Nieuwe naam scenario",
            "Enter new scenario name",
            "Enter new scenario name",
            "Enter new scenario name",
            "Enter new scenario name",
        ]
        self.new_name: List[str] = ["New name for ", "Neuer Name für ", "Nieuwe naam voor ", "New name for ", "New name for ", "New name for ", "New name for "]
        self.label_okay: List[str] = ["Okay ", "Okay ", "Oke ", "Okay ", "Okay ", "Okay ", "Okay "]
        self.label_abort: List[str] = ["Abort ", "Abbruch ", "Geannuleerd ", "Abort ", "Abort ", "Abort ", "Abort "]
        self.NoBackupFile: List[str] = [
            "no backup fileImport",
            "Keine Sicherungsdatei gefunden",
            "geen backup fileImport",
            "no backup fileImport",
            "no backup fileImport",
            "no backup fileImport",
            "no backup fileImport",
        ]
        self.pushButton_borehole_resistance: List[str] = [
            "Borehole\\nresistance",
            "Bohrloch-\\nwiderstand",
            "Boorgat-\\nweerstand",
            "Borehole\\nresistance",
            "Borehole\\nresistance",
            "Borehole\\nresistance",
            "Borehole\\nresistance",
        ]
        self.label_Spanish: List[str] = ["Spanish", "Spanisch", "Spaans", "Spanish", "Spanish", "Spanish", "Spanish"]
        self.label_Galician: List[str] = ["Galician", "Galizisch", "Galisisch", "Galician", "Galician", "Galician", "Galician"]
        self.label_close: List[str] = ["Close", "Schließen", "Sluit", "Close", "Close", "Close", "Close"]
        self.label_cancel: List[str] = ["Cancel", "Abbrechen", "Annuleer", "Cancel", "Cancel", "Cancel", "Cancel"]
        self.label_CancelTitle: List[str] = ["Warning", "Warnung", "Waarschuwing", "Warning", "Warning", "Warning", "Warning"]
        self.label_LeaveScenarioText: List[str] = [
            "Are you sure you want to leave scenario? Any unsaved work will be lost.",
            "Bist du sicher das Szenario zu verlasen? Alle ungesicherten Änderungen gehen sonst verloren.",
            "Bent u zeker dat u het scenario wilt verlaten?Onopgeslagen werk kan verloren gaan.",
            "Are you sure you want to leave scenario? Any unsaved work will be lost.",
            "Are you sure you want to leave scenario? Any unsaved work will be lost.",
            "Are you sure you want to leave scenario? Any unsaved work will be lost.",
            "Are you sure you want to leave scenario? Any unsaved work will be lost.",
        ]
        self.label_LeaveScenario: List[str] = [
            "Leave scenario",
            "Szenario verlassen",
            "Verlaat scenario",
            "Leave scenario",
            "Leave scenario",
            "Leave scenario",
            "Leave scenario",
        ]
        self.label_StayScenario: List[str] = [
            "Stay by scenario",
            "Beim Szenario bleiben",
            "Blijf bij scenario",
            "Stay by scenario",
            "Stay by scenario",
            "Stay by scenario",
            "Stay by scenario",
        ]
        self.X_Axis_Load: List[str] = [
            "Month of year",
            "Monat des Jahres",
            "Maand van het jaar",
            "Month of year",
            "Month of year",
            "Month of year",
            "Month of year",
        ]
        self.Y_Axis_Load_P: List[str] = [
            "Remaining peak thermal power [kW]",
            "Übriggebliebene Spitzenleistung [kW]",
            "Overblijvende piek [kW]",
            "Remaining peak thermal power [kW]",
            "Remaining peak thermal power [kW]",
            "Remaining peak thermal power [kW]",
            "Remaining peak thermal power [kW]",
        ]
        self.Y_Axis_Load_Q: List[str] = [
            "Remaining thermal energy [kWh]",
            "Übriggebliebene thermische Last [kWh]",
            "Overblijvende energie energy [kWh]",
            "Remaining thermal energy [kWh]",
            "Remaining thermal energy [kWh]",
            "Remaining thermal energy [kWh]",
            "Remaining thermal energy [kWh]",
        ]
        self.label_aim: List[str] = [
            "Aim of simulation",
            "Ziel der Simulation",
            "Doel van de berekening",
            "Aim of simulation",
            "Aim of simulation",
            "Aim of simulation",
            "Aim of simulation",
        ]
        self.menuLanguage: List[str] = ["Language", "Sprache", "Taal", "Languange", "Languange", "Idiom", "Lingua"]
        self.menuSettings: List[str] = ["Settings", "Einstellungen", "Instellingen", "Settings", "Settings", "Settings", "Settings"]
        self.menuCalculation: List[str] = ["Calculation", "Berechnung", "Berekening", "Calculation", "Calculation", "Calculation", "Calculation"]
        self.menuFile: List[str] = ["File", "Datei", "Bestand", "File", "File", "File", "File"]
        self.menuScenario: List[str] = ["Scenario", "Szenario", "Scenario", "Scenario", "Scénario", "Escenario", "Escenario"]
        self.action_start_multiple: List[str] = [
            "Calculate all scenarios",
            "Berechne alle Szenarios",
            "Bereken alle scenarios",
            "Calculate all scenarios",
            "Calculate all scenarios",
            "Calculate all scenarios",
            "Calculate all scenarios",
        ]
        self.actionGerman: List[str] = ["German", "Deutsch", "Duits", "German", "German", "German", "German"]
        self.actionEnglish: List[str] = ["English", "Englisch", "Engels", "English", "English", "English", "English"]
        self.actionDutch: List[str] = ["Dutch", "Niederländisch", "Nederlands", "Dutch", "Dutch", "Dutch", "Dutch"]
        self.actionFrench: List[str] = ["French", "Französisch", "Frans", "French", "French", "French", "French"]
        self.actionItalian: List[str] = ["Italian", "Italienisch", "Italiaans", "Italian", "Italian", "Italian", "Italian"]
        self.actionNew: List[str] = ["New Project", "Neues Projekt", "Nieuw project", "New Project", "New Project", "New Project", "New Project"]
        self.actionSave: List[str] = ["Save Project", "Speichere Projekt", "Bewaar project", "Save Project", "Save Project", "Save Project", "Save Project"]
        self.actionOpen: List[str] = ["Open Project", "Öffne Projekt", "Open project", "Open Project", "Open Project", "Open Project", "Open Project"]
        self.actionUpdate_Scenario: List[str] = [
            "Update scenario",
            "Szenario aktualisieren",
            "Update scenario",
            "Aggiorna scenario",
            "Mettre à jour le scénario",
            "Actualizar escenario",
            "Actualizar escenario",
        ]
        self.actionAdd_Scenario: List[str] = [
            "Add scenario",
            "Szenario hinzufügen",
            "Nieuw scenario",
            "Aggiungi scenario",
            "Ajouter un scénario",
            "Añadir escenario",
            "Engadir escenario",
        ]
        self.actionDelete_scenario: List[str] = [
            "Delete scenario",
            "Szenario löschen",
            "Verwijder scenario",
            "Cancella scenario",
            "Supprimer un scénario",
            "Borrar escenario",
            "Eliminar escenario",
        ]
        self.actionSave_As: List[str] = ["Save as", "Speichere Projekt unter ...", "Sla op als", "Save as", "Save as", "Save as", "Save as"]
        self.actionRename_scenario: List[str] = [
            "Rename scenario",
            "Szenario umbenennen",
            "Hernoem scenario",
            "Rename scenario",
            "Rename scenario",
            "Rename scenario",
            "Rename scenario",
        ]
        self.button_rename_scenario: List[str] = [
            "Rename scenario",
            "Szenario umbenennen",
            "Hernoem scenario",
            "Rename scenario",
            "Rename scenario",
            "Rename scenario",
            "Rename scenario",
        ]
        self.label_Language_Head: List[str] = ["Language", "Sprache", "Taal", "Languange", "Languange", "Idiom", "Lingua"]
        self.label_aim_question: List[str] = [
            "What is the purpose of the simulation?",
            "Was ist das Ziel der Simulation?",
            "Wat is het doel van de berekening?",
            "What is the purpose of the simulation?",
            "What is the purpose of the simulation?",
            "What is the purpose of the simulation?",
            "What is the purpose of the simulation?",
        ]
        self.pushButton_PreviousResistance: List[str] = [
            "  previous  ",
            "  vorheriges  ",
            "  vorige  ",
            "  precedente  ",
            "  précédente  ",
            "  anterior  ",
            "  anterior  ",
        ]
        self.pushButton_NextResistance: List[str] = [
            "  next  ",
            "  nächstes  ",
            "  volgende  ",
            "  successivo  ",
            "  suivant  ",
            "  siguiente  ",
            "  seguinte  ",
        ]
        self.comboBox_AimList: List[str] = [
            "['Determine temperature profile', 'Determine required depth', 'Size bore field by length and width', 'Optimize load profile']",
            "['Bestimme Temperaturprofil', 'Bestimme notwendige Tiefe', 'Dimensioniere Bohrfeld nach Länge und Breite', 'Optimiere Lastprofil']",
            "['Bepaal temperatuursprofiel', 'Bepaal de benodigde diepte', 'Dimensioneer boorveld bij lengte en breedte', 'Optimaliseer belastingsprofiel']",
            "['Determine temperature profile', 'Determine required depth', 'Size bore field by length and width', 'Optimize load profile']",
            "['Determine temperature profile', 'Determine required depth', 'Size bore field by length and width', 'Optimize load profile']",
            "['Determine temperature profile', 'Determine required depth', 'Size bore field by length and width', 'Optimize load profile']",
            "['Determine temperature profile', 'Determine required depth', 'Size bore field by length and width', 'Optimize load profile']",
        ]
        self.label_Seperator: List[str] = [
            "Seperator in CSV-fileImport:",
            "Trenner in der CSV-Datei:",
            "Scheidingsteken in CSV-fileImport:",
            "Seperator in CSV-fileImport:",
            "Seperator in CSV-fileImport:",
            "Seperator in CSV-fileImport:",
            "Seperator in CSV-fileImport:",
        ]
        self.label_SeperatorDataFile: List[str] = [
            "Seperator in CSV-fileImport:",
            "Trenner in der CSV-Datei:",
            "Scheidingsteken in CSV-fileImport:",
            "Seperator in CSV-fileImport:",
            "Seperator in CSV-fileImport:",
            "Seperator in CSV-fileImport:",
            "Seperator in CSV-fileImport:",
        ]
        self.comboBox_SeperatorList: List[str] = [
            "[\"Semicolon ';'\", \"Comma ','\"]",
            "[\"Semikolon ';'\", \"Komma ','\"]",
            "[\"Puntkomma ';'\", \"Komma ','\"]",
            "[\"Semicolon ';'\", \"Comma ','\"]",
            "[\"Semicolon ';'\", \"Comma ','\"]",
            "[\"Semicolon ';'\", \"Comma ','\"]",
            "[\"Semicolon ';'\", \"Comma ','\"]",
        ]
        self.label_data_file: List[str] = [
            "Select data fileImport",
            "Wähle Datendatei",
            "Selecteer data fileImport",
            "Select data fileImport",
            "Select data fileImport",
            "Select data fileImport",
            "Select data fileImport",
        ]
        self.label_Filename_2: List[str] = [
            "Filename: ",
            "Dateiname: ",
            "Bestandsnaam: ",
            "Nome fileImport: ",
            "Nom de fichier: ",
            "Nombre de archivo: ",
            "Nome de ficheiro: ",
        ]
        self.label_dataColumn_2: List[str] = [
            "Thermal demands: ",
            "Thermische Lasten: ",
            "Thermische vraag: ",
            "Richieste termiche: ",
            "Demande thermique: ",
            "Cargas térmicas: ",
            "Cargas térmicas: ",
        ]
        self.label_HeatingLoadLine_2: List[str] = [
            "Heating load line: ",
            "Heizlastspalte: ",
            "Belastingslijn verwarming: ",
            "Linea di carico di riscaldamento: ",
            "Ligne de charge de chauffage: ",
            "Línea de carga de calefacción: ",
            "Liña de carga de calefacción: ",
        ]
        self.label_CoolingLoadLine_2: List[str] = [
            "Cooling load line: ",
            "Kühllastspalte: ",
            "Belastingslijn koeling: ",
            "Linea del carico di raffreddamento: ",
            "Ligne de charge de refroidissement: ",
            "Línea de carga de refrigeración: ",
            "Liña de carga de refrixeración: ",
        ]
        self.label_combined_2: List[str] = [
            "Load line: ",
            "Load line: ",
            "Belastingslijn: ",
            "Linea di carico: ",
            "Ligne de charge: ",
            "Línea de carga: ",
            "Liña de carga: ",
        ]
        self.label_DataUnit_2: List[str] = [
            "Unit data: ",
            "Dateneinheit: ",
            "Eenheid data: ",
            "Dati \\ndell'unità:  ",
            "Données de l'unité: ",
            "Datos de unidad: ",
            "Datos de unidade: ",
        ]
        self.label_Scenario_Head: List[str] = [
            "Scenario saving settings",
            "Szenarioeinstellungen für das Speichern",
            "Instellingen opslaan scenario",
            "Scenario saving settings",
            "Scenario saving settings",
            "Scenario saving settings",
            "Scenario saving settings",
        ]
        self.checkBox_AutoSaving: List[str] = [
            "Automatic saving",
            "Automatisches speichern",
            "Automatisch opslaan",
            "Automatic saving",
            "Automatic saving",
            "Automatic saving",
            "Automatic saving",
        ]
        self.label_Scenario_Hint: List[str] = [
            "If Auto saving is selected the scenario will automatically saved if a scenario is changed. Otherwise the scenario has to be saved with the Update scenario button in the upper left corner if the changes should not be lost.",
            "Wenn Automatisch speichern ausgewählt ist, wird das Szenario automatisch gespeichert, wenn ein Szenario geändert wird. Andernfalls muss das Szenario mit der Schaltfläche Szenario aktualisieren in der oberen linken Ecke gespeichert werden, wenn die Änderungen nicht verloren gehen sollen.",
            'Als auto-opslaan is geselecteerd, zal het scenario automatisch worden opgeslagen alshet wordt gewijzigd. Anders kan het scenario opgeslagen worden als op de "update scenario"-kopwordt gedrukt als deze niet verloren mogen gaan.',
            "If Auto saving is selected the scenario will automatically saved if a scenario is changed. Otherwise the scenario has to be saved with the Update scenario button in the upper left corner if the changes should not be lost.",
            "If Auto saving is selected the scenario will automatically saved if a scenario is changed. Otherwise the scenario has to be saved with the Update scenario button in the upper left corner if the changes should not be lost.",
            "If Auto saving is selected the scenario will automatically saved if a scenario is changed. Otherwise the scenario has to be saved with the Update scenario button in the upper left corner if the changes should not be lost.",
            "If Auto saving is selected the scenario will automatically saved if a scenario is changed. Otherwise the scenario has to be saved with the Update scenario button in the upper left corner if the changes should not be lost.",
        ]
        self.label_Borehole_Resistance: List[str] = [
            "Equivalent borehole resistance",
            "Equivalänter Bohrlochwiderstand",
            "Equivalente boorgatweerstand",
            "Equivalent borehole resistance",
            "Equivalent borehole resistance",
            "Equivalent borehole resistance",
            "Equivalent borehole resistance",
        ]
        self.label_Borehole_Resistance_Head: List[str] = [
            "Equivalent borehole resistance",
            "Equivalänter Bohrlochwiderstand",
            "Equivalente boorgatweerstand",
            "Equivalent borehole resistance",
            "Equivalent borehole resistance",
            "Equivalent borehole resistance",
            "Equivalent borehole resistance",
        ]
        self.label_Rb_calculation_method: List[str] = [
            "Calculation method:",
            "Berechnungsmethode:",
            "Berekeningsmethode:",
            "Calculation method:",
            "Calculation method:",
            "Calculation method:",
            "Calculation method:",
        ]
        self.comboBox_Rb_methodList: List[str] = [
            "['Known constant value', 'Unknown constant value', 'During calculation updating value']",
            "['Bekannter konstanter Wert', 'Unbekannter konstanter Wert', 'Während der Berechnung aktualisierender Wert']",
            "['Constante waarde (gegeven)', 'Constante waarde (berekend)', 'Dynamische waarde']",
            "['Known constant value', 'Unknown constant value', 'During calculation updating value']",
            "['Known constant value', 'Unknown constant value', 'During calculation updating value']",
            "['Known constant value', 'Unknown constant value', 'During calculation updating value']",
            "['Known constant value', 'Unknown constant value', 'During calculation updating value']",
        ]
        self.label_fluid_data: List[str] = ["Fluid data", "Fluiddaten", "Fluidumdata", "Fluid data", "Fluid data", "Fluid data", "Fluid data"]
        self.label_fluid_lambda: List[str] = [
            "Thermal conductivity [W/mK]: ",
            "Wärmeleitfähigkeit [W/mK]: ",
            "Thermische conductiviteit [W/mK]: ",
            "Thermal conductivity [W/mK]: ",
            "Thermal conductivity [W/mK]: ",
            "Thermal conductivity [W/mK]: ",
            "Thermal conductivity [W/mK]: ",
        ]
        self.label_fluid_mass_flow_rate: List[str] = [
            "Mass flow rate [kg/s]: ",
            "Massenstrom [kg/s]: ",
            "Massadebiet [kg/s]: ",
            "Mass flow rate [kg/s]: ",
            "Mass flow rate [kg/s]: ",
            "Mass flow rate [kg/s]: ",
            "Mass flow rate [kg/s]: ",
        ]
        self.label_fluid_density: List[str] = [
            "Density [kg/m³]:",
            "Dichte [kg/m³]:",
            "Dichtheid [kg/m³]:",
            "Density [kg/m³]:",
            "Density [kg/m³]:",
            "Density [kg/m³]:",
            "Density [kg/m³]:",
        ]
        self.label_fluid_thermal_capacity: List[str] = [
            "Thermal capacity [J/kg K]:",
            "Wärmekapazität [J/kg K]:",
            "Thermalisch warmtecapaciteit [J/kg K]:",
            "Thermal capacity [J/kg K]:",
            "Thermal capacity [J/kg K]:",
            "Thermal capacity [J/kg K]:",
            "Thermal capacity [J/kg K]:",
        ]
        self.label_fluid_viscosity: List[str] = [
            "Dynamic viscosity [Pa s]:",
            "Dynamische Viskosität [Pa s]:",
            "Dynamische viscositeit [Pa s]:",
            "Dynamic viscosity [Pa s]:",
            "Dynamic viscosity [Pa s]:",
            "Dynamic viscosity [Pa s]:",
            "Dynamic viscosity [Pa s]:",
        ]
        self.label_pipe_data: List[str] = ["Pipe data", "Rohrdaten", "Boorgatdata", "Pipe data", "Pipe data", "Pipe data", "Pipe data"]
        self.label_NumberOfPipes: List[str] = [
            "Number of pipes [#]:",
            "Anzahl an Rohren [#]:",
            "Aantal U-buizen [#]:",
            "Number of pipes [#]:",
            "Number of pipes [#]:",
            "Number of pipes [#]:",
            "Number of pipes [#]:",
        ]
        self.label_grout_conductivity: List[str] = [
            "Grout thermal conductivity [W/mK]: ",
            "Wärmeleitfähigkeit der Füllung [W/mK]: ",
            "Thermische conductiviteit van de vulling [W/mK]: ",
            "Grout thermal conductivity [W/mK]: ",
            "Grout thermal conductivity [W/mK]: ",
            "Grout thermal conductivity [W/mK]: ",
            "Grout thermal conductivity [W/mK]: ",
        ]
        self.label_pipe_conductivity: List[str] = [
            "Pipe thermal conductivity [W/mK]: ",
            "Wärmeleitfähigkeit der Rohre [W/mK]: ",
            "Thermische conductiviteit van de leiding [W/mK]: ",
            "Pipe thermal conductivity [W/mK]: ",
            "Pipe thermal conductivity [W/mK]: ",
            "Pipe thermal conductivity [W/mK]: ",
            "Pipe thermal conductivity [W/mK]: ",
        ]
        self.label_pipe_outer_radius: List[str] = [
            "Outer pipe radius [m]: ",
            "Äußerer Rohrradius [m]: ",
            "Straal buitenkant leiding [m]: ",
            "Outer pipe radius [m]: ",
            "Outer pipe radius [m]: ",
            "Outer pipe radius [m]: ",
            "Outer pipe radius [m]: ",
        ]
        self.label_pipe_inner_radius: List[str] = [
            "Inner pipe radius [m]: ",
            "Innerer Rohrradius [m]: ",
            "Straal binnenkant leiding [m]: ",
            "Inner pipe radius [m]: ",
            "Inner pipe radius [m]: ",
            "Inner pipe radius [m]: ",
            "Inner pipe radius [m]: ",
        ]
        self.label_borehole_radius: List[str] = [
            "Borehole radius [m]:",
            "Bohrlochradius [m]:",
            "Boorgatstraal [m]:",
            "Borehole radius [m]:",
            "Borehole radius [m]:",
            "Borehole radius [m]:",
            "Borehole radius [m]:",
        ]
        self.label_pipe_distance: List[str] = [
            "Distance of pipe until center [m]:",
            "Distanz zwischen Rohr und Mittelpunkt [m]:",
            "Afstand van de leiding tot het centrum van het boorgat [m]:",
            "Distance of pipe until center [m]:",
            "Distance of pipe until center [m]:",
            "Distance of pipe until center [m]:",
            "Distance of pipe until center [m]:",
        ]
        self.label_pipe_roughness: List[str] = [
            "Pipe roughness [m]:",
            "Rohrrauhigkeit [m]:",
            "Ruwheid leiding [m]:",
            "Pipe roughness [m]:",
            "Pipe roughness [m]:",
            "Pipe roughness [m]:",
            "Pipe roughness [m]:",
        ]
        self.label_borehole_burial_depth: List[str] = [
            "Burial depth [m]:",
            "Vergrabungstiefe [m]:",
            "Begraven diepte [m]:",
            "Burial depth [m]:",
            "Burial depth [m]:",
            "Burial depth [m]:",
            "Burial depth [m]:",
        ]
        self.label_ResOptimizeLoad1: List[str] = [
            "The peak heating / cooling load is: ",
            "Die Spitzenheiz-/kühllast ist: ",
            "De piek verwarming / koeling is: ",
            "The peak heating / cooling load is: ",
            "The peak heating / cooling load is: ",
            "The peak heating / cooling load is: ",
            "The peak heating / cooling load is: ",
        ]
        self.label_ResOptimizeLoad2: List[str] = [
            "The heating / cooling load is: ",
            "Die Heiz-/Kühllast: ",
            "De belasting in verwarming / koeling is: ",
            "The heating / cooling load is:  ",
            "The heating / cooling load is: ",
            "The heating / cooling load is: ",
            "The heating / cooling load is: ",
        ]
        self.label_ResOptimizeLoad3: List[str] = ["This is ", "Dies ist ", "Dit is ", "This is ", "This is ", "This is ", "This is "]
        self.label_ResOptimizeLoad4: List[str] = [
            "% of the total load. ",
            "% der kompletten Last. ",
            "% van de totale belasting. ",
            "% of the total load. ",
            "% of the total load. ",
            "% of the total load. ",
            "% of the total load. ",
        ]
        self.label_CancelText: List[str] = [
            "Are you sure you want to quit? Any unsaved work will be lost.",
            "Bist du sicher das Programm zu schließen? Alle ungesicherten Änderungen gehen sonst verloren.",
            "Bent u zeker dat u wilt afsluiten? Niet opgeslagen wijzigingen zullen verloren gaan.",
            "Are you sure you want to quit? Any unsaved work will be lost.",
            "Are you sure you want to quit? Any unsaved work will be lost.",
            "Are you sure you want to quit? Any unsaved work will be lost.",
            "Are you sure you want to quit? Any unsaved work will be lost.",
        ]
        self.label_ResOptimizeLoad5: List[str] = [
            "The remaining peak heating / cooling load is: ",
            "Die übrigbleibende Spitzenheiz-/kühllast ist: ",
            "De resulterende piek in verwarming / koeling is: ",
            "The remaining peak heating / cooling load is: ",
            "The remaining peak heating / cooling load is: ",
            "The remaining peak heating / cooling load is: ",
            "The remaining peak heating / cooling load is: ",
        ]
        self.label_ResOptimizeLoad6: List[str] = [
            "The remaining heating / cooling load is: ",
            "Die übrigbleibende Heiz-/Kühllast:  ",
            "De resulterende belasting in verwarming / koeling is: ",
            "The remaining heating / cooling load is: ",
            "The remaining heating / cooling load is: ",
            "The remaining heating / cooling load is: ",
            "The remaining heating / cooling load is: ",
        ]
        self.pushButton_start_single: List[str] = [
            "Calculate current scenario",
            "Berechne ausgewähltes Szenario",
            "Bereken huidig scenario",
            "Calculate current scenario",
            "Calculate current scenario",
            "Calculate current scenario",
            "Calculate current scenario",
        ]
        self.NotCalculated: List[str] = [
            "Not calculated",
            "Noch nicht berechnet",
            "Niet berekend",
            "Not calculated",
            "Not calculated",
            "Not calculated",
            "Not calculated",
        ]
        self.NoSolution: List[str] = [
            "No Solution found",
            "Keine Lösung gefunden",
            "Geen oplossing gevonden",
            "No Solution found",
            "No Solution found",
            "No Solution found",
            "No Solution found",
        ]
        self.comboBox_decimalList: List[str] = [
            "[\"Point '.'\", \"Comma ','\"]",
            "[\"Punkt '.'\", \"Komma ','\"]",
            "[\"Punt '.'\", \"Komma ','\"]",
            "[\"Point '.'\", \"Comma ','\"]",
            "[\"Point '.'\", \"Comma ','\"]",
            "[\"Point '.'\", \"Comma ','\"]",
            "[\"Point '.'\", \"Comma ','\"]",
        ]
        self.label_decimalDataFile: List[str] = [
            "Decimal sign in CSV-fileImport:",
            "Dezimalzeichen in CSV-Datei:",
            "Decimaal teken in de CSV-fileImport:",
            "Decimal sign in CSV-fileImport:",
            "Decimal sign in CSV-fileImport:",
            "Decimal sign in CSV-fileImport:",
            "Decimal sign in CSV-fileImport:",
        ]
        self.label_decimal: List[str] = [
            "Decimal sign in CSV-fileImport:",
            "Dezimalzeichen in CSV-Datei:",
            "Decimaal teken in de CSV-fileImport:",
            "Decimal sign in CSV-fileImport:",
            "Decimal sign in CSV-fileImport:",
            "Decimal sign in CSV-fileImport:",
            "Decimal sign in CSV-fileImport:",
        ]
        self.actionSpanish: List[str] = ["Spanish", "Spanisch", "Spaans", "Spanish", "Spanish", "Spanish", "Spanish"]
        self.actionGalician: List[str] = ["Galician", "Galizisch", "Galisisch", "Galician", "Galician", "Galician", "Galician"]
