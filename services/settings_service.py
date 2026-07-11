import config


class SettingsService:
    def update_settings(self, interest, start_chit, end_chit):
        config.interest_value = float(interest)
        config.Start_chit = str(start_chit)
        config.End_Chit = str(end_chit)

    def get_settings(self):
        return {
            "interest_value": config.interest_value,
            "Start_chit": config.Start_chit,
            "End_Chit": config.End_Chit,
            "chit_no": config.chit_no
        }

