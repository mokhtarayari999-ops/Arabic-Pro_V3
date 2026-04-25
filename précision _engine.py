# ملف: precision_engine.py
def calculate_precision(o1, ox, o2):
    # حساب القوة الفعلية للسوق (حذف هامش ربح المكتب)
    total_power = (1/o1) + (1/ox) + (1/o2)
    
    # حساب الاحتمالات الحقيقية بدقة 3 خانات
    prob_1 = (1/o1) / total_power
    prob_x = (1/ox) / total_power
    prob_2 = (1/o2) / total_power
    
    # حساب الحساسية (Market Shift) بدقة 0.001
    precise_shift = total_power - 1.000
    
    return {
        "shift": round(precise_shift, 3),
        "draw_p": round(prob_x * 100, 1) # نسبة التعادل بدقة
  }
  
