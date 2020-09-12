# NASA-Semantic-Search-Engine-for-Scientific-Literature
NASA DT Hackathon

## Setup
### BERT Model
1. Cloned the entire repository
``` 
git clone https://github.com/vizzies/NASA-Semantic-Search-Engine-for-Scientific-Literature.git
cd NASA-Semantic-Search-Engine-for-Scientific-Literature
```
2. Open a Google Colab Environment and import `semantic-search.ipynb`
3. Go into `edit` > `notebook settings` under `hardware accelerator` left `GPU`
4. To run each cell, press `shift` + `return`
5. Under the heading `BERT Sentence Transformer Semantic Search`, in the `queries` list, add your scientific query of choice
6. Run that cell to recieve searched literature documents

### Figma Mockup
1. Create background frame `#F3F3F3` for web application
2. Add in search bar for semantic query search
3. Add title and hackathon team logo into the pseudo-navigation bar
4. Add placeholder for advanced search (future implementation)
5. Create cards for publications. Metadata received on card preview includes:
    * publish dates
    * abstract character length
    * entered query in search bar
    * relevancy score
    * main author(s)
6. Place pagination varibales at the end
7. Place page navigation number


## Repository File Directory
