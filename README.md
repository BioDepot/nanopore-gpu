# nanopore-gpu

## Setup
The project folders correspond to BioDepot-workflow-builder (BWB) workflows. BWB can be found and installed [here](https://github.com/BioDepot/BioDepot-workflow-builder).

## Overview
These workflows offer a graphical and GPU-enabled platform that supports interactive and reproducible execution of long-read sequencing data. 

## Data Links
<ol>
  <li><a href="https://drive.google.com/drive/folders/1tYN8oDKNiMRQLNzQrpdljmAIumikyYkG?usp=sharing">NB4-(PML-RARA) </a></li>
  <li><a href="https://drive.google.com/drive/folders/1Tq2qCmbtqCCEcN9xQ4xU-5c50dpOXtcg?usp=sharing">K562-(BCR-ABL1) </a></li>
  <li><a href="https://drive.google.com/drive/folders/1S0HvJcPCKpivUGMyVRq91WQhCUA9WY40?usp=sharing">CRISPR-ME1</a></li>
  <li><a href="https://drive.google.com/drive/folders/18jBPVRAtFLOcLcoN-j_y2OYT4jUjdsJF?usp=sharing">CRISPR-MV411</a></li>
</ol>

### Guppy Workflow
#### Widgets
<ol>
  <li>Download: Used for downloading fast5 files or other starting data by providing a download link and output folder.</li> 
  <li>Setup Guppy: Since Guppy is a proprietary basecaller, the <a href="https://nanoporetech.com/">ONT</a> Guppy Software Download link needs to be provided by the user. This widget will proceed to download and install Guppy after the link is provided.</li> 
  <li>Guppy (proprietary basecaller): After entering the required parameters (input-output directories and the specified model file), Guppy basecalling will proceed. It is highly recommended to use the GPU-enabled Guppy by marking the "Use GPU" checkbox before starting the widget.</li>
  <li>Index (<a href="https://github.com/lh3/minimap2">Minimap2</a>): Before aligning, it is required to create an index (.mmi) of the reference genome being used. This widget uses minimap2 to create an index which can then be used in the alignment step.</li>
  <li>Align ( <a href="https://github.com/lh3/minimap2">Minimap2</a> + <a href="http://www.htslib.org/">Samtools</a> ): This widget uses minimap2 to align the basecalled reads to a reference genome, then sorts and indexes the output with Samtools. The resulting bam files are saved in the specified output directory.</li>
  <li>View alignments (<a href="https://software.broadinstitute.org/software/igv/">IGV</a>): The resulting bam files from alignment can be viewed within Integrated Genomics Viewer in this widget.</li>
</ol>

### Bonito Workflow
The Bonito workflow is identical to the Guppy Workflow post-basecalling. In the basecalling step, no setup widget is necessary because Bonito is a research-grade basecaller and all setup can be done without user intervention.
