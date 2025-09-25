#!/bin/bash
#SBATCH --job-name=isntall # Job name
#SBATCH --mail-type=END,FAIL # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=u6596617@anu.edu.au # Where to send mail
#SBATCH --ntasks=1 # Run on a single CPU
#SBATCH --mem=8G # Job memory request
#SBATCH --time=00:15:00 # Time limit hrs:min:sec
#SBATCH --partition=teaching
#SBATCH --gres=gpu:1
#SBATCH --output=install_%j.log # Standard output and error log


singularity exec --nv /opt/apps/containers/tensorflow_21.10-tf2-py3.sif pip3 install --user matplotlib
