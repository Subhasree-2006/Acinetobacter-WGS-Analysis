# Workflow: Whole Genome and Structural Analysis of Acinetobacter baumannii (SRR5891469)

## Overview
This workflow describes the complete bioinformatics pipeline used for genomic characterization, antimicrobial resistance profiling, virulence factor identification, OXA-23 mutation analysis, protein structure prediction, and structural validation.

## Workflow Steps

### Data Acquisition
- NCBI SRA Dataset (SRR5891469)
- Reference Genome: NZ_CP045110.1

### 1. Quality Assessment (FastQC)
### 2. Read Trimming (FastP)
### 3. Read Alignment (BWA-MEM)
### 4. Alignment Processing (SAMtools)
### 5. Variant Calling (BCFtools)
### 6. Genome Annotation (Prokka)
### 7. AMR Gene Identification (ABRicate CARD/NCBI)
### 8. Virulence Factor Identification (ABRicate VFDB)
### 9. OXA-23 Extraction
### 10. Mutation Analysis of OXA-23
### 11. IGV Validation
### 12. Protein Structure Prediction (SWISS-MODEL)
### 13. Structure Validation (PROCHECK, ERRAT, Verify3D)
### 14. Integrated Analysis
### 15. Biological Interpretation
### 16. Conclusion

## Software Used
- FastQC
- FastP
- BWA-MEM
- SAMtools
- BCFtools
- Prokka
- ABRicate
- IGV
- SWISS-MODEL
- PROCHECK
- ERRAT
- Verify3D
