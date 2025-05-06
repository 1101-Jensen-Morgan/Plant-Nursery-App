import pytest
from unittest.mock import patch, MagicMock
import tkinter as tk
from app.FinalProjectApplication import (
    verifyUniqeUser,
    verifyUserCred,
    varifyingResults,
    log_entry,
    addNewPlant,
    remove_plant,
    load_user_plants_widgets,
    loadWaterings,
    addNewWat
)

class TestHelperFunctions:

    @patch('app.FinalProjectApplication.fpd.getUserNames')
    def test_verifyUniqeUser_unique(self, mock_get_names):
        mock_get_names.return_value = [('existing1',), ('existing2',)]
        assert verifyUniqeUser('new_user') is True

    @patch('app.FinalProjectApplication.fpd.getUserNames')
    def test_verifyUniqeUser_not_unique(self, mock_get_names):
        mock_get_names.return_value = [('existing1',), ('existing2',)]
        assert verifyUniqeUser('existing1') is False

    @patch('app.FinalProjectApplication.fpd.getPassword')
    def test_verifyUserCred_correct(self, mock_get_pass):
        mock_get_pass.return_value = 'correct_pass'
        assert verifyUserCred('user', 'correct_pass') is True

    @patch('app.FinalProjectApplication.fpd.getPassword')
    def test_verifyUserCred_incorrect(self, mock_get_pass):
        mock_get_pass.return_value = 'correct_pass'
        assert verifyUserCred('user', 'wrong_pass') is False

    @patch('app.FinalProjectApplication.verifyUserCred')
    @patch('app.FinalProjectApplication.Load_Frame_Home')
    @patch('app.FinalProjectApplication.fpd.getUserID')
    def test_varifyingResults_success(self, mock_get_id, mock_load, mock_verify):
        mock_verify.return_value = True
        mock_get_id.return_value = 1
        root = MagicMock()
        frame = MagicMock()
        varifyingResults(root, frame, 'user', 'pass')
        mock_load.assert_called_once()

    @patch('app.FinalProjectApplication.verifyUniqeUser')
    @patch('app.FinalProjectApplication.fpd.new_user')
    @patch('app.FinalProjectApplication.Load_Frame_Home')
    @patch('app.FinalProjectApplication.fpd.getUserID')
    def test_log_entry_success(self, mock_get_id, mock_load, mock_new_user, mock_verify):
        mock_verify.return_value = True
        mock_get_id.return_value = 1
        root = MagicMock()
        frame = MagicMock()
        new_user_window = MagicMock()
        log_entry(root, frame, new_user_window, 'new', 'pass', 'first', 'last')
        mock_new_user.assert_called_once()
        mock_load.assert_called_once()

    @patch('app.FinalProjectApplication.fpd.new_plant')
    @patch('app.FinalProjectApplication.load_user_plants_widgets')
    def test_addNewPlant(self, mock_load, mock_new_plant):
        user_plants_frame = MagicMock()
        new_plant_window = MagicMock()
        addNewPlant(user_plants_frame, new_plant_window, 'plant', 1)
        mock_new_plant.assert_called_once_with(1, 'plant')
        mock_load.assert_called_once()

    @patch('app.FinalProjectApplication.fpd.remove_plant')
    @patch('app.FinalProjectApplication.load_user_plants_widgets')
    def test_remove_plant(self, mock_load, mock_remove):
        remove_window = MagicMock()
        user_plants_frame = MagicMock()
        remove_plant(remove_window, user_plants_frame, 1, 2)
        mock_remove.assert_called_once_with(2, 1)
        mock_load.assert_called_once()

    @patch('app.FinalProjectApplication.fpd.getUserPlants')
    @patch('app.FinalProjectApplication.fpd.getPlantNames')
    @patch('app.FinalProjectApplication.fpd.getPlantInfo')
    @patch('app.FinalProjectApplication.tk.IntVar')
    @patch('app.FinalProjectApplication.tk.Radiobutton')
    @patch('app.FinalProjectApplication.tk.Label')
    @patch('app.FinalProjectApplication.tk.Text')
    @patch('app.FinalProjectApplication.tk.Button')
    def test_load_user_plants_widgets(self, mock_button, mock_text, mock_label, 
                                    mock_radio, mock_var, mock_info, mock_names, mock_plants):
        mock_plants.return_value = [1, 2]
        mock_names.return_value = ['Plant1', 'Plant2']
        mock_info.return_value = [None]*11
        mock_var.return_value = MagicMock()
        
        # Create a real frame with mock children
        frame = MagicMock()
        frame.winfo_children.return_value = []
        
        load_user_plants_widgets(frame, 1)
        
        # Verify widgets were created
        mock_label.assert_called_once()  # Main label
        mock_text.assert_called_once()   # Text widget
        assert mock_radio.call_count >= 2  # Radio buttons for plants
        mock_button.assert_called()      # Add/remove buttons

    @patch('app.FinalProjectApplication.fpd.getWatLog')
    @patch('app.FinalProjectApplication.tk.Label')
    @patch('app.FinalProjectApplication.tk.Button')
    @patch('app.FinalProjectApplication.tk.Listbox')
    def test_loadWaterings(self, mock_list, mock_button, mock_label, mock_log):
        mock_log.return_value = [
            (1, '2023-01-01', 10, False, None, 1, 1),
            (2, '2023-01-02', 8, True, 2, 1, 1)
        ]
        
        # Create a real frame with mock children
        frame = MagicMock()
        frame.winfo_children.return_value = []
        
        loadWaterings(frame, 1)
        
        # Verify widgets were created
        mock_label.assert_called_once()  # Main label
        mock_button.assert_called_once() # New record button
        mock_list.assert_called_once()   # Listbox for records