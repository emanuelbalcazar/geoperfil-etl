import spacy
from spacy import displacy
from spacy.pipeline import EntityRuler


def find_charges():

    nlp = spacy.load('es_core_news_md')

    ruler = EntityRuler(nlp)

    pattern = [{"label": "CARGO", "pattern": "rector"},
            {"label": "CARGO", "pattern": "Rector"},
            {"label": "CARGO", "pattern": "rectora"},
            {"label": "CARGO", "pattern": "Rectora"},
            {"label": "CARGO", "pattern": "rectores"},
            {"label": "CARGO", "pattern": "Rectores"},
           {"label": "CARGO", "pattern": "vicerector"},
           {"label": "CARGO", "pattern": "Vicerector"},
            {"label": "CARGO", "pattern": "vicerectora"},
            {"label": "CARGO", "pattern": "Vicerector"},
            {"label": "CARGO", "pattern": "delegado"},
           {"label": "CARGO", "pattern": "Delegado"},
           {"label": "CARGO", "pattern": "delegada"},
           {"label": "CARGO", "pattern": "Delegada"},
           {"label": "CARGO", "pattern": "delegado zonal"},
           {"label": "CARGO", "pattern": "Delegado zonal"},
           {"label": "CARGO", "pattern": "delegado Zonal"},
           {"label": "CARGO", "pattern": "Delegado Zonal"},
           {"label": "CARGO", "pattern": "delegada zonal"},
           {"label": "CARGO", "pattern": "Delegada zonal"},
           {"label": "CARGO", "pattern": "Delegada Zonal"},
           {"label": "CARGO", "pattern": "delegada Zonal"},
           {"label": "CARGO", "pattern": "cantautor"},
           {"label": "CARGO", "pattern": "Cantautor"},
           {"label": "CARGO", "pattern": "cantautora"},
           {"label": "CARGO", "pattern": "Cantautor"},
           {"label": "CARGO", "pattern": "consejo directivo"},
           {"label": "CARGO", "pattern": "Consejo directivo"},
           {"label": "CARGO", "pattern": "consejo Directivo"},
           {"label": "CARGO", "pattern": "Consejo Directivo"},
           {"label": "CARGO", "pattern": "consejo departamental"},
           {"label": "CARGO", "pattern": "Consejo departamental"},
           {"label": "CARGO", "pattern": "Consejo Departamental"},
           {"label": "CARGO", "pattern": "consejo Departamental"},
           {"label": "CARGO", "pattern": "secretario"},
           {"label": "CARGO", "pattern": "Secretario"},
           {"label": "CARGO", "pattern": "secretaria"},
           {"label": "CARGO", "pattern": "Secretarioa"},
           {"label": "CARGO", "pattern": "secretarios"},
           {"label": "CARGO", "pattern": "Secretarios"},
           {"label": "CARGO", "pattern": "director"},
           {"label": "CARGO", "pattern": "Director"},
           {"label": "CARGO", "pattern": "directora"},
           {"label": "CARGO", "pattern": "Directora"},
           {"label": "CARGO", "pattern": "directores"},
           {"label": "CARGO", "pattern": "Directores"},
           {"label": "CARGO", "pattern": "familiares"},
           {"label": "CARGO", "pattern": "Familiares"},
           {"label": "CARGO", "pattern": "familiar"},
           {"label": "CARGO", "pattern": "Familiar"},
           {"label": "CARGO", "pattern": "decano"},
           {"label": "CARGO", "pattern": "Decano"},
           {"label": "CARGO", "pattern": "decana"},
           {"label": "CARGO", "pattern": "Decano"},
           {"label": "CARGO", "pattern": "vicedecano"},
           {"label": "CARGO", "pattern": "Vicedecano"},
           {"label": "CARGO", "pattern": "vicedecana"},
           {"label": "CARGO", "pattern": "Vicedecano"},
           {"label": "CARGO", "pattern": "secretario"},
           {"label": "CARGO", "pattern": "Secretario"},
           {"label": "CARGO", "pattern": "secretaria"},
           {"label": "CARGO", "pattern": "Secretaria"},
           {"label": "CARGO", "pattern": "coro"},
           {"label": "CARGO", "pattern": "Coro"},
           {"label": "CARGO", "pattern": "cantautor"},
           {"label": "CARGO", "pattern": "Cantautor"},
           {"label": "CARGO", "pattern": "cantautora"},
           {"label": "CARGO", "pattern": "Cantautora"},
           {"label": "CARGO", "pattern": "cantante"},
           {"label": "CARGO", "pattern": "Cantante"},
           {"label": "CARGO", "pattern": "bombista"}]

    ruler.add_patterns(pattern)

    nlp.add_pipe(ruler)


    article = """
El rector De Marziani se refirió a los problemas económicos que atraviesan las universidades y recordó la lucha que llevan adelante en defensa de la educación pública y gratuita. 
La Universidad Nacional de la Patagonia San Juan Bosco realizó el acto académico de la CLVIII Colación de Grado, en donde recibieron sus títulos 252 nuevos profesionales.
Además también se realizó la LXIII Colación de Posgrado donde siete personas recibieron sus diplomas. Martín Frixione y Gabriel Punta recibieron su título de doctor en Ciencias Biológicas; Silvana Fronza es especialista en Contaminación de Aguas Subterráneas:
Silvina Grill y Gustavo Trigo en especialistas en Ciencias Químicas con mención en Diagnóstico Ambiental; y por último los magister en  Gestión Empresaria María Righero y Gustavo Navarro.
El acto estuvo encabezado por el rector dr. Carlos Manuel De Marziani, y las autoridades de las cinco facultades. La Facultad con mayor cantidad de egresados fue Cs. Naturales y Cs. de la Salud con 131 nuevos profesionales. Hubo 51 egresados de Ingeniería; 14 egresados de Cs. Económicas; 38 de Humanidades y Cs. Sociales; y 17 de Cs. Jurídicas.
  6
Defensa de la Universidad pública
En el discurso de apertura, De Marziani felicitó a los nuevos egresados, señaló que el 50% de ellos recibió durante su carrera alguna de las becas estudiantiles que ofrece la casa de altos estudios, y asimismo hizo hincapié en la defensa de la educación pública y gratuita. En otro orden también se refirió a que el 70% del estudiantado son mujeres; “estamos en la era de las mujeres, la lucha entre una verdadera igualdad entre géneros y la paridad en la política, gremios, empresas y demás espacios es responsabilidad de todos, desde la universidad nos toca formar en este pensamiento” expresó.
Destacó que el sistema universitario nacional argentino es admirado y replicado en varios países de Latinoamérica y el resto del mundo, donde se han formado premios Nobel y científicos de renombre mundial.
En este marco, también recordó la lucha que llevaron adelante durante todo el año docentes, no docentes y estudiantes, a través de marchas, clases públicas y distintas actividades para visibilizar la problemática actual en defensa del sistema público, gratuito y de calidad.
Crisis financiera
Al respecto de la situación financiera, el rector indicó que en los últimos tiempos atravesaron situaciones de restricciones económicas: “la incertidumbre de transferencias de fondos para gastos de funcionamiento, la no ejecución de planillas complementarias destinadas a mejoras de infraestructura, el envío de montos inferiores a lo pautado, el congelamiento de obras pautadas hace más de dos años, la demora en el cierre de los acuerdos salariales que permitan a los trabajadores universitarios recuperar el poder adquisitivo en un contexto de alta inflación y devaluación”. Asimismo se refirió a las complicaciones del incremento de costos de servicios, bienes y equipamiento necesario para su funcionamiento.
"""
        
    doc = nlp( article )

    charges = [token.text for token in doc.ents if token.label_ == "CARGO"]
    charges = list( set( charges ) )
    print ("Cargos: ", charges )

    persons = [token.text for token in doc.ents if (token.label_ == "PER")]
    persons = list( set( persons ) )
    print ("Personas: ", persons) 

    article = article.replace(',', ' ')
    article = article.replace('.', ' ')
    article = article.replace(';', ' ')

    words = article.split()
    print ( 'cantidad de palabras: ' + str( len( words ) ))
   
    charge_positions = [[]]
    for charge in charges:
        pos = []
        for i in range(0, len(words)):
            if words[i] == charge:
                pos.append( i )
        charge_positions.append( [charge, pos ] )
        
    print( 'cargos posiciones: ' + str( charge_positions ) )

    person_positions = [[]]
    for person in persons:
        pos = []
        for i in range(0,len(words)):
            if words[i] == person:
                pos.append( i )
        person_positions.append( [person, pos] )
    print( 'personas posiciones: ' + str( person_positions ) )

    #charges_persons = []
    #or charge in charge_positions:
     #   for pos_charge in range(0,len( charge )):
      #      for person in person_positions:
       #         for pos_person in range( 9,len( person ) ):
        #            if pos_person - pos_charge > 0 and pos_person - pos_charige <= 5:
         #               charges_persons.append( charge, person )
    
    #print( 'cargos persona: ' + str( charges_persons ))
            
    colors = {"PER": "linear-gradient(90deg,#FFFF00,#00FFFF)"}
    options = {"colors": colors}
    displacy.serve(doc, style="ent", options=options)


find_charges()