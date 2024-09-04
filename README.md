# proyectos

Objetivo: 1 año, 100 proyectos
Progreso: 3 / 100

## Reglas

- Se publica a `producción`, no hay staging (por ahora)
- Los cambios son `hotfixes`
- El pipeline lo más simple posible: considerando gestionarlo con PM2
- Se suben todas las webs al mismo servidor
- TODO: programar backups en nube y otro disco

---

1. 31.08.24: [Temporizador con Tkinter](./01/)
  
  **Desktop**
  
  - Se puede usar para aplicar pomodoro en el trabajo
  - Reproduce un sonido al llegar a `00:00:00`

2. 01.09.24: [Proyecto Django para gestionar logs de trabajo](./02/)
  
  **Terminal**
  
  - Carga logs de txt con un script si hay histórico anterior
  - Guardar logs en db
  - Lista de logs, form pare crear nuevo log

3. 02.09.24: [Scrapping de pisos](./03/)
  
  **Terminal** _Salida en TXT_

  - Se puede calcular la distancia de varias ciudades a una dirección
  - Scrapping de página de pisos para obtener ofertas
  - TODO: incluir enlace a publicación en resultados y ordenar resultados
  - TODO: bucle para scrapear toda la web usando lista de ciudades

4. 04.09.24: [Benchmark de servidores web](./04/)
  **Terminal** _reporte de resultados en PDF_
  - Benchmark de GET de 10, 100, 1000, 10_000 usuarios en el mismo formato en HTML
  - Django:
    - sirviendo templates
    - solo API
    - lectura de JSON
    - lectura de DB local
  - PHP (template y datos)
  - Go (template y datos)
  - TODO: Compilar PDF con resultados

5. dd.mm.yy: [nombre](./05/)
  - 
  - Feature 02
  - Feature 03