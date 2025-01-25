class AI_Agent:
    """
    סוכן AI המספק ייעוץ לגבי השקעות.
    """
    def __init__(self, risk_level):
        """
        אתחול סוכן ה-AI עם רמת סיכון מירבית.
        :param risk_level: רמת הסיכון המקסימלית שהסוכן מאפשר
        """
        self.risk_level = risk_level

    def get_advice(self, security):
        """
        נותן ייעוץ אם להשקיע בנייר ערך מסוים על בסיס רמת הסיכון.
        :param security: אובייקט של מניה או אג"ח
        :return: מילון עם אישור (True/False) וסיבה
        """
        if not hasattr(security, "calculate_risk"):
            return {"approved": False, "reason": "האובייקט אינו מכיל פונקציה לחישוב סיכון."}

        # חישוב רמת הסיכון של נייר הערך
        risk = security.calculate_risk()
        
        # בדיקה אם רמת הסיכון גבוהה מהרמה המותרת
        if risk > self.risk_level:
            return {
                "approved": False,
                "reason": f"רמת הסיכון {risk:.2f} גבוהה מדי עבור הרמה המותרת {self.risk_level:.2f}."
            }
        
        return {
            "approved": True,
            "reason": "השקעה מאושרת. רמת הסיכון במסגרת המותר."
        }
