# Self Instruct for Health and Fitness Finetune Dataset

The aim of this repo is to create Instruction Finetune dataset for health and fitness domain using an idea from self instruct paper. self instruct is  a framework for improving
the instruction-following capabilities of pretrained language models by bootstrapping off their own generations. 



## Data Set Creation

### Creating seed tasks 
1. I have considered three broader categories for creating Health and Fitness Instruction Data . \
        a. Physical Health \
        b. Mental Health \
        c. Fitness 

2. I have created more categories for each broader categories . I have attached a Google sheets [[file](./Instruction_Data_Categories.xlsx)] where you can find all the categories of each broader categories. 
3. I have created a one seed question for each sub categories and used that dataset and seed dataset to create multiple diverse instructions, inputs and Output.  


### Creating Dataset
                                 Flow of Self Instruct Framework 
![self_instruct_flow](self_instruct.png)

In the self instruct paper, authors have created 175 seed tasks , I have created 40 seed tasks for health and fitness. We will select few random seed tasks and append these tasks to a prompt in prompt.txt file and ask GPT Model to create few more instructions with diverse tasks from the seed tasks.\
We preprocess these new generated tasks and append them in regen.json file. you can repeat this process by running generate_instruction.py file until you reach the required size of your dataset.


# Installation

1.Clone the GitHub Repo into your local workspace using the below code.
```sh
git clone https://github.com/ramachaitanya0/self_instruct.git
```

2.Create a Conda Environment.
```sh
conda create -n <env_name> python=3.10.14
```

3.Activate the conda Environment
```sh
conda activate <env_name> 
```

4.Install all the required Packages using requirements.txt file.
```sh
pip install -r requirements.txt
```
5.Add .env file in the Repo and add your OPEN AI Key, mail id and password in .env file.
```sh
OPENAI_API_KEY=<OPENAI_API_KEY>
```

# Usage

Run the python file using below code.
```sh
python -m generate_instruction generate_instruction_following_data
```




## Acknowledgements

 * Most of this code is derived from [[tatsu-lab](https://github.com/tatsu-lab)]'s [[stanford_alpaca](https://github.com/tatsu-lab/stanford_alpaca)], which is licensed under the Apache License, Version 2.0.
 * The full text of the license can be found in the LICENSE file included with this distribution.
 * I have Modified few files to create required datasets based on requirement.
 * If you want to read the paper of Self Instruct this is the self instruct paper [[link](https://arxiv.org/pdf/2212.10560.pdf)]


