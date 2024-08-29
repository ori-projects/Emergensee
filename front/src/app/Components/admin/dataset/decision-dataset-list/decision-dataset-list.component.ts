import { Component, Output, EventEmitter, OnInit } from '@angular/core';
import { Decisiondataset } from '../../../../Modules/decision-dataset/decision-dataset.module';
import { ApiService } from '../../../../Services/api.service';

@Component({
  selector: 'app-decision-dataset-list',
  templateUrl: './decision-dataset-list.component.html',
  styleUrls: ['./decision-dataset-list.component.css']
})
export class DecisiondatasetListComponent implements OnInit {
  @Output() selectdataset: EventEmitter<Decisiondataset> = new EventEmitter<Decisiondataset>();
  datasets: Decisiondataset[] = [];
  selecteddataset: Decisiondataset | null = null;

  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.fetchDatasets();
  }

  fetchDatasets() {
    this.apiService.getDatasets().subscribe(
      (response: any) => {
        this.datasets = Object.keys(response.datasets).map(key => response.datasets[key]);
      },
      error => {
        console.error('Error fetching datasets:', error);
      }
    );
  }

  ondatasetelect(dataset: Decisiondataset) {
    this.selecteddataset = dataset;
    this.selectdataset.emit(dataset);
  }
}