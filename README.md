# Semantic Search Engine for Scientific Literature
[NASA DT Hackathon](https://dthack.spaceappschallenge.org)  
By the Vizzies (GVIS)

**Challenge**: Develop an intelligent literature search and analysis application that reads NASA-relevant scientific articles using natural language processing and text mining, returns knowledge analysis and relevant scientific findings, and reveals knowledge gaps and multi-disciplinary research opportunities.  
**Time Frame**: about **15 hours**

## Setup
### BERT Model - `Semantic-Search.ipynb`
1. Clone the entire repository
``` 
$ git clone https://github.com/vizzies/NASA-Semantic-Search-Engine-for-Scientific-Literature.git
$ cd NASA-Semantic-Search-Engine-for-Scientific-Literature
```
2. Open a Google Colab Environment and import `semantic-search.ipynb`
3. Go into `edit` > `notebook settings` under `hardware accelerator` and select `GPU`
4. To run each cell, press `SHIFT` + `Return`
5. Under the heading `BERT Sentence Transformer Semantic Search`, in the `queries` list, add your scientific query of choice
6. Run that cell to recieve searched literature documents

### Figma Mockup - [Clickable Prototype](https://www.figma.com/file/8McMiR3Eo8ccFVowPE8Hcy/Semantic-Search-Engine-for-Scientific-Literature-by-Vizzies?node-id=0%3A1)
1. Create a background frame `#F3F3F3` for web application
2. Add in search bar for semantic query search
3. Add title and hackathon team logo into the pseudo-navigation bar
   * create footer similarly
4. Add placeholder for advanced search (future implementation?)
5. Create data cards for returned results of publications. Metadata received on card preview includes:
    * publish dates
    * abstract character length
    * relevancy score
    * main author(s)
6. Place pagination function buttons `previous` and `next` at the bottom
   * emphasize current page navigation number at bottom of page
7. Export CSS code from each object mentioned above for Flask front-end implementation
   * select object > go to `code` in side menu > `CRTL` + `c`

### Flask Application Setup
A microservice written in Python with the [Flask micro framework](http://flask.pocoo.org). Source code located at https://github.com/vizzies/bertsearch.

#### Contents
1. [Set Up Environment](#set_up_env)
    1. [`virtualenv` environment](#virtualenv)
    2. [`conda` environment](#conda)
2. [Initialize Flask App](#init_flask)

&nbsp;
#### Set Up Environment <a name="set_up_env"></a>
##### `virtualenv` environment <a name="virtualenv"></a>

1. Clone the repo
```bash
git clone https://github.com/vizzies/bertsearch.git
```
2. `cd` into the new directory
```bash
cd bertsearch
```
3. Initiate a new virtual environment and store in the project's `env` directory
```bash
python -m virtualenv env
```
4. Activate the new virtual environment
```bash
source env/bin/activate
```
5. Install dependencies in new environment
```bash
pip install -r requirements.txt
```
&nbsp;
##### `conda` environment <a name="conda"></a>
1. Clone the repo
```bash
git clone https://github.com/vizzies/bertsearch.git
```
2. `cd` into the new directory
```bash
cd bertsearch
```
3. Create a new conda environment in the project's `env` directory
```bash
conda create python=3.8.3 --prefix ./env
```
4. Activate the new environment
```bash
conda activate ./env
```
5. Install dependencies in new environment
```bash
pip install -r requirements.txt
```
#### Initialize Flask App <a name="init_flask"></a>

3. Initialize the app database
```bash
flask db init
```
4. Generate the first database migration
```bash
flask db migrate
```
5. Run database the migration `upgrade` script
```bash
flask db upgrade
```
6. Run the flask app
```bash
flask run
```
7. You should now be able to make a call to your API. Paste this URL into your browser and check for a valid response
```bash
http://127.0.0.1:8080/api/v1/results
```

## Contributors

* Herb Schilling, GRC, Computer Scientist, [hschilling@nasa.gov](hschilling@nasa.gov)
* Calvin Robinson, GRC, Data Architect, [calvin.r.robinson@nasa.gov](calvin.r.robinson@nasa.gov)
* Evan "Taylor" Yates, MSFC, Software Engineer, [evan.t.yates@nasa.gov](evan.t.yates@nasa.gov)
* Gulsum Oz, ARC, Information Tech Specialist, [oz.gulsum@nasa.gov](oz.gulsum@nasa.gov)
* Shruti Janardhanan, GRC, Intern, [shruti.janardhanan@nasa.gov](shruti.janardhanan@nasa.gov)
* Kelci Mensah, GRC, Intern, [kelci.mensah@nasa.gov](kelci.mensah@nasa.gov)
* Samantha "Sam" Stesch, GRC, Intern, [samantha.g.stesch@nasa.gov](samantha.g.stesch@nasa.gov)
* Heather Sulier, GRC, Intern, [heather.sulier@nasa.gov](heather.sulier@nasa.gov)
