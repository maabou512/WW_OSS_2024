# Convert XLSX dataset into JSON (2024 World of Open Source: Global Spotlight)

## Motivation
* Want to analyze open source dynamism in more sophisticated way than Excel
* Want to analyze focusing on Japan 

## About dataset
* Convert survey rawdata(xlsx) into json data objects. 
* Survey rawdata:  [2024 World of Open Source: Global Spotlight](https://data.world/thelinuxfoundation/2024-world-of-open-source-global-spotlight) 
* Output json data: Please refer [here](https://data.world/maabou512/lf-2024-world-of-open-source-global-spotlight-json-data)(data.world)

## Procedure as a whole
### 1. Manual modification
Too sad, some "hand work" is necessary because question's header(line 1-3 of xlsx file) are different about depth/layers. So you need modify header line 2 with line 3 info for Q30,31,32,38,42,43,47.

Example: (in Q30 case);
The line 2 item 
> "How often does using OSS deliver the following benefits in your organization? (select one response per row)" 

is modified with the line 3 item to; 

> "How often does using OSS deliver the following benefits in your organization? (select one response per row):*Improved software quality*" 

then you save the file as "input_files/input.csv"

### 2. Run script "run_pipeline.py"
Just run it. 

### 3. Register datasets into Opensearch/Elasticsearch 
example:

```curl -s  -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/index_name/_bulk?pretty --data-binary @output_1l_bulk.json```

### 4. Configure and analyze 
Configure settings and do analyze on Opensearch Dashboard/Kibana

## Scripts
* run_pipeline.py : Main and run following scripts and shell commands.(bash)  

* step1.py: modified csv file extracted from original excel.
<pre>
  *In: input_files/input.csv
  *Out: output_files/output_step1.csv
</pre>
* step2.py: change timestamp into ISO formats (from 'yyyy-MM-dd HH:mm:ss' to 'yyyy-MM-ddT HH:mm:ss'
<pre>
  *In: output_files/output_step1.csv
  *Out: output_files/output_step2.csv
</pre>
* step3.py: convert csv into json
<pre>
  *In: output_files/output_step2.csv
  *Out: output_files/output_step3.json
</pre>

* cmd1: extract each data object  from array (`cat *In* |jq -c .[] >  *Out*`)
<pre>
  *In: output_files/output_step3.json
  *Out: output_files/output_per_line.json
</pre>
* cmd2: Change json to register Opensearch/Elasticsearch and use Bulk API(`sed 'i\{ "index" : {} \}  *In*' > *Out*`　)
<pre>
  *In: output_files/output_per_line.json
  *Out: output_files/output_bulk.json
</pre>

### Directories
<pre>
/
│
├── scripts/
│   ├── step1.py
│   ├── step2.py
│   ├── step3.py
│   └── run_pipeline.py
│
├── input_files/
│   └── input.csv
│
├── output_files/
│   └── output*.*
│
└── README.md
</pre>

### My environments
* Ubuntu 22.04LTS
* Python 3.11.0 
* bash : 5.1.16

### Others
* Unlicense 