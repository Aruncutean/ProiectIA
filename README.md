<h1>Proiect IA</h1>

<h2>Detectarea obiectelor intr-o imagine cu YOLOv8 si Roboflow</h1>

<h3>Descriere</h3>
 Acest proiect utilizează algoritmi avansați de învățare automată pentru a detecta și identifica canile într-o varietate de imagini. Scopul principal este de a demonstra capacitatea tehnologiei de recunoaștere a obiectelor, cu un accent specific pe cani.

<h3>Tehnologii </h3>
<h4>YOLOv8</h4> Folosim versiunea a opta a framework-ului YOLO (You Only Look Once) pentru detectarea obiectelor în timp real, datorită preciziei și vitezei sale remarcabile.
 <h4>Roboflow</h4> Utilizăm Roboflow pentru a prelucra și a organiza setul de date de imagini, facilitând antrenarea modelului nostru de învățare automată.

<h3> Instalare și Configurare </h3>
Am separat proiectul in doua etape: <br>
<ol>
    <li>in identificarea setului de date</li> 
   <li> in antrenarea modelului </li>
</ol>
<h2>1.Identificarea setului de date</h2>   
<ol>
 <li>Pentru identificarea setului de date am utilizat Roboflow. Roboflow este o platformă specializată în computer vision care facilitează procesul de creare, distribuție și utilizare a seturilor de date pentru antrenarea modelelor de învățare automată. Principalul său scop este de a simplifica și de a optimiza procesul de dezvoltare pentru proiecte de viziune artificială.</li>
<li>Am selectat imaginii de pe google </li>

<img src="https://github.com/Aruncutean/ProiectIA/assets/52048476/ce3fef68-15ef-45f5-8b28-e600a353dc38" width="800" />
 <li>Am creat un nou proiect in roboflow  </li>

<img src="https://github.com/Aruncutean/ProiectIA/assets/52048476/f148ddf0-d372-4106-8fb4-28a987fad4d3" width="600" />
 <li>Am updatat imaginile selectate in roboflow  </li>


<img src="https://github.com/Aruncutean/ProiectIA/assets/52048476/a5948ba6-904a-4fa8-94ea-8ea5beae5931" width="600" />
 <li>Dupa am folosit functia de ANNOTATE pentru a delimita obiectele de interes  </li>
 

<img src="https://github.com/Aruncutean/ProiectIA/assets/52048476/67151fa2-8aee-402c-9b71-002c8ef02cfb" width="600" />
<li>Dupa am exportat datele pentru a le utiliza in colab </li>


<img src="https://github.com/Aruncutean/ProiectIA/assets/52048476/6991ec3c-847e-4aa3-b6b7-87b776cb37b8" width="600" />

</ol>


<h2>1.Antrenarea modelului</h2>
<ol>
  <li>
  Pentru antrenarea modelului am utilizat colab de la google, si am urmat pasi din tutorialul acesta
  </li>
  

<img src="https://github.com/Aruncutean/ProiectIA/assets/52048476/ce12001b-dcd5-481a-8007-7cff83d93078" width="600" />
 <li>Before you start </li>


<img src="https://github.com/Aruncutean/ProiectIA/assets/52048476/66527519-03b2-4773-8ea4-1f5d66f7f27d" width="600" />
<li>Install YOLOv8 </li>


<img src="https://github.com/Aruncutean/ProiectIA/assets/52048476/73fcdbfe-2580-47db-8308-697038741197" width="600" />
<li>Exporting dataset</li>


<img src="https://github.com/Aruncutean/ProiectIA/assets/52048476/e4154fd0-4ee9-40ac-a386-965311e83848" width="600" />
<li>Ce nu apare in tutorial am editat path-urile catre fisierele exportate din roboflow</li>


<img src="https://github.com/Aruncutean/ProiectIA/assets/52048476/15d4bdcb-ff88-4258-9d51-c18282794e29" width="600" />
<li>Custom Training</li>
 <img src="https://github.com/Aruncutean/ProiectIA/assets/52048476/b0d891dd-3478-4e7f-9342-574189dcc5d3" width="600" />
</ol>

<h3>Rezultate obitinute</h3>

<h5>Am antrenat reteaua pentru mai multe tipuri de modele dintre care: </h5>
<ol>
   <li>YOLOv8n </li>
  <p float="left">
  <img src="https://github.com/Aruncutean/ProiectIA/assets/52048476/0bcbbb74-0087-4e3e-b3be-21d039f8404b" width="400" />
  <img src="https://github.com/Aruncutean/ProiectIA/assets/52048476/58a9ded3-db4c-4bf4-9e24-4e2e643f0223" width="400" /> 
</p>
 <img src="https://github.com/Aruncutean/ProiectIA/assets/52048476/97542672-5c47-4dd2-9c45-401a54b334ff" width="600" /> 


   <li>YOLOv8s </li>
  <p float="left">
  <img src="https://github.com/Aruncutean/ProiectIA/assets/52048476/0bcbbb74-0087-4e3e-b3be-21d039f8404b" width="400" />
  <img src="https://github.com/Aruncutean/ProiectIA/assets/52048476/e2caaa86-cb9a-4cd3-ad43-a808c8664e97" width="400" /> 
</p>
 <img src="https://github.com/Aruncutean/ProiectIA/assets/52048476/c5f5d3cc-d682-49a9-87bc-3ec4356a619b" width="600" /> 
   <li>YOLOv8m epochs=58 </li>
 <p float="left">
  <img src="https://github.com/Aruncutean/ProiectIA/assets/52048476/0bcbbb74-0087-4e3e-b3be-21d039f8404b" width="400" />
  <img src="https://github.com/Aruncutean/ProiectIA/assets/52048476/e2caaa86-cb9a-4cd3-ad43-a808c8664e97" width="400" /> 
</p>
 <img src="https://github.com/Aruncutean/ProiectIA/assets/52048476/c5f5d3cc-d682-49a9-87bc-3ec4356a619b" width="600" /> 

   <li>YOLOv8l </li>
    <p float="left">
  <img src="https://github.com/Aruncutean/ProiectIA/assets/52048476/0bcbbb74-0087-4e3e-b3be-21d039f8404b" width="400" />
  <img src="https://github.com/Aruncutean/ProiectIA/assets/52048476/e2caaa86-cb9a-4cd3-ad43-a808c8664e97" width="400" /> 
</p>
 <img src="https://github.com/Aruncutean/ProiectIA/assets/52048476/c5f5d3cc-d682-49a9-87bc-3ec4356a619b" width="600" /> 
</ol>



