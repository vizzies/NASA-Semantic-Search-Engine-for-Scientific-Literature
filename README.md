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

### Figma Mockup
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
1.


## Repository File Directory

## Contributors

* Herb Schilling, GRC, Computer Scientist, [hschilling@nasa.gov](hschilling@nasa.gov)
* Calvin Robinson, GRC, Data Architect, [calvin.r.robinson@nasa.gov](calvin.r.robinson@nasa.gov)
* Evan "Taylor" Yates, MSFC, Software Engineer, [evan.t.yates@nasa.gov](evan.t.yates@nasa.gov)
* Gulsum Oz, ARC, Information Tech Specialist, [oz.gulsum@nasa.gov](oz.gulsum@nasa.gov)
* Shruti Janardhanan, GRC, Intern, [shruti.janardhanan@nasa.gov](shruti.janardhanan@nasa.gov)
* Kelci Mensah, GRC, Intern, [kelci.mensah@nasa.gov](kelci.mensah@nasa.gov)
* Samantha "Sam" Stesch, GRC, Intern, [samantha.g.stesch@nasa.gov](samantha.g.stesch@nasa.gov)
* Heather Sulier, GRC, Intern, [heather.sulier@nasa.gov](heather.sulier@nasa.gov)
