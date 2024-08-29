import { Component, Input, OnChanges, SimpleChanges } from '@angular/core';
import { Decisiondataset } from '../../../../Modules/decision-dataset/decision-dataset.module';

@Component({
  selector: 'app-decision-dataset-detail',
  templateUrl: './decision-dataset-detail.component.html',
  styleUrls: ['./decision-dataset-detail.component.css']
})
export class DecisiondatasetDetailComponent implements OnChanges {
  @Input() selecteddataset: Decisiondataset | null = null;
  selectedModel: any;

  ngOnChanges(changes: SimpleChanges): void {
    if (!changes.selecteddataset.currentValue)
      return;
    
    this.selectedModel = null;
  }

  showModelDetails(model: any) {
    this.selectedModel = model;
  }
}