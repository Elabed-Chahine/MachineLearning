from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Disease(models.Model):
    SYMPTOMS=(('itching','itching'), ('skin rash','skin rash'),( 'nodal skin eruptions', 'nodal skin eruptions'),
       ('continuous sneezing','continuous sneezing'), ('shivering','shivering'),( 'chills', 'chills'), ('joint pain','joint pain'),
      ( 'stomach pain', 'stomach pain'), ('acidity','acidity'), ('ulcers on tongue','ulcers on tongue'), ('muscle wasting','muscle wasting'),
       ('vomiting','vomiting'), ('burning micturition','burning micturition'), ('spotting urination','spotting urination'), ('fatigue','fatigue'),
      ( 'weight gain', 'weight gain'),( 'anxiety', 'anxiety'),( 'cold hands and feets', 'cold hands and feets'), ('mood swings','mood swings'),
       ('weight loss','weight loss'),( 'restlessness', 'restlessness'), ('lethargy','lethargy'), ('patches in throat','patches in throat'),
       ('irregular sugar level','irregular sugar level'), ('cough','cough'))

    SYMPTOMS2=(('high fever','high fever'), ('high fever','high fever'),
       ('breathlessness','breathlessness'),( 'sweating', 'sweating'), ('dehydration','dehydration'), ('indigestion','indigestion'),
       ('headache','headache'), ('yellowish skin','yellowish skin'), ('dark urine','dark urine'), ('nausea','nausea'),
       ('loss of appetite','loss of appetite'), ('pain behind the eyes','pain behind the eyes'),( 'back pain', 'back pain'),
       ('constipation','constipation'),('constipation','constipation'), ('diarrhoea','diarrhoea'), ('mild fever','mild fever'),
       ('yellow urine','yellow urine'), ('yellowing of eyes','yellowing of eyes'),( 'acute liver failure', 'acute liver failure'))

    SYMPTOMS3=(
       ('fluid overload','fluid overload'), ('swelling of stomach','swelling of stomach'),( 'swelled lymph nodes', 'swelled lymph nodes'),
       ('malaise','malaise'), ('blurred and distorted vision','blurred and distorted vision'), ('phlegm','phlegm'),
       ('throat irritation','throat irritation'), ('redness of eyes','redness of eyes'), ('sinus pressure','sinus pressure'),
       ('runny nose','runny nose'),( 'congestion', 'congestion'), ('chest pain','chest pain'), ('weakness in limbs','weakness in limbs'),
       ('fast heart rate','fast heart rate'), ('pain during bowel movements','pain during bowel movements'))

    SYMPTOMS4=(
       ('pain in anal region','pain in anal region'), ('bloody stool','bloody stool'), ('irritation in anus','irritation in anus'),
       ('neck pain','neck pain'), ('dizziness','dizziness'), ('cramps','cramps'),( 'bruising', 'bruising'), ('obesity','obesity'),
      ( 'swollen legs', 'swollen legs'),( 'swollen blood vessels', 'swollen blood vessels'), ('puffy face and eyes','puffy face and eyes'),
      ( 'enlarged thyroid', 'enlarged thyroid'), ('brittle nails','brittle nails'), ('swollen extremeties','swollen extremeties'),
       ('excessive hunger','excessive hunger'),( 'extra marital contacts', 'extra marital contacts'),
       ( 'extra marital contacts', 'extra marital contacts'), ('slurred speech','slurred speech'), ('knee pain','knee pain'))

    SYMPTOMS5=( ('hip joint pain','hip joint pain'),('hip joint pain','hip joint pain'), ('stiff neck','stiff neck'),
      ( 'swelling joints', 'swelling joints'), ('movement stiffness','movement stiffness'), ('spinning movements','spinning movements'),
       ('loss of balance','loss of balance'), ('unsteadiness','unsteadiness'), ('weakness of one body side','weakness of one body side'),
       ('loss of smell','loss of smell'), ('bladder discomfort','bladder discomfort'), ('foul smell ofurine','foul smell ofurine'),
       ('continuous feel of urine','continuous feel of urine'),( 'passage of gases', 'passage of gases'), ('internal itching','internal itching'),
       ('toxic look (typhos)','toxic look (typhos)'),( 'depression', 'depression'), ('irritability','irritability'),( 'muscle pain', 'muscle pain'),
       ('altered sensorium','altered sensorium'),( 'red spots over body', 'red spots over body'), ('belly pain','belly pain'),
       ('abnormal menstruation','abnormal menstruation'), ('dischromic patches','dischromic patches'))

    
    
    SYMPTOMS6=(('watering from eyes','watering from eyes'), ('increased appetite','increased appetite'), ('polyuria','polyuria'),
       ('family history','family history'), ('mucoid sputum','mucoid sputum'), ('rusty sputum','rusty sputum'),
       ('lack of concentration','lack of concentration'),( 'visual disturbances', 'visual disturbances'),
       ('receiving blood transfusion','receiving blood transfusion'), ('receiving unsterile injections','receiving unsterile injections'),
       ('coma','coma'), ('stomach bleeding','stomach bleeding'), ('distention of abdomen','distention of abdomen'),
       ('history of alcohol consumption','history of alcohol consumption'), ('blood in sputum','blood in sputum'))
    

    SYMPTOMS7=(('prominent veins on calf','prominent veins on calf'), ('palpitations','palpitations'), ('painful walking','painful walking'),
       ('pus filled pimples','pus filled pimples'), ('blackheads','blackheads'), ('scurring','scurring'), ('skin peeling','skin peeling'),
       ('silver like dusting','silver like dusting'), ('small dents in nails','small dents in nails'),
       ('inflammatory nails','inflammatory nails'),( 'blister', 'blister'), ('red sore around nose','red sore around nose'),
      ( 'yellow crust ooze', 'yellow crust ooze'), ('prognosis','prognosis'))

    
    symptom1 = models.CharField(choices=SYMPTOMS, max_length=255, blank=True)
    symptom2 = models.CharField(choices=SYMPTOMS2, max_length=255, blank=True)
    symptom3 = models.CharField(choices=SYMPTOMS3, max_length=255, blank=True)
    symptom4 = models.CharField(choices=SYMPTOMS4, max_length=255, blank=True)
    symptom5 = models.CharField(choices=SYMPTOMS5, max_length=255, blank=True)
    symptom6 = models.CharField(choices=SYMPTOMS6, max_length=255, blank=True)
    symptom7 = models.CharField(choices=SYMPTOMS7, max_length=255, blank=True)
    sickness= models.CharField( max_length=255)
   
    def __str__(self):
        return ('Disease') 




class Comment(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   body= models.TextField(max_length=500)
   created = models.DateTimeField(auto_now_add=True)
   def __str__(self):
      return self.body[0:50]
    
