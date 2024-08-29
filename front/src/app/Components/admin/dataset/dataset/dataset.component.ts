import { Component } from '@angular/core';
import { Decisiondataset } from '../../../../Modules/decision-dataset/decision-dataset.module';

@Component({
  selector: 'app-dataset',
  templateUrl: './dataset.component.html',
  styleUrl: './dataset.component.css'
})
export class datasetComponent {
  selecteddataset: Decisiondataset | null = null;
  constructor() {}
  
  onSelectdataset(dataset: Decisiondataset) {
    this.selecteddataset = dataset;
  }
}