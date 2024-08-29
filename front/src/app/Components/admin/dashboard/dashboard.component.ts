import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../../Services/api.service';

interface Endpoint {
  name: string;
  status: string;
}

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  endpoints: Endpoint[] = [
    { name: 'Accounts', status: 'Unknown' },
    { name: 'Admins', status: 'Unknown' },
    { name: 'Algorithms', status: 'Unknown' },
    { name: 'DatasetOps', status: 'Unknown' },
    { name: 'Datasets', status: 'Unknown' },
    { name: 'Doctors', status: 'Unknown' },
    { name: 'Models', status: 'Unknown' },
    { name: 'Patients', status: 'Unknown' },
    { name: 'Widgets', status: 'Unknown' },
    { name: 'Utils', status: 'Unknown' }
  ];
  selectedEndpoint: Endpoint | null = null;

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.fetchEndpointStatuses();
  }

  fetchEndpointStatuses(): void {
    this.apiService.checkAccountsServiceHealth().subscribe(
      () => this.updateEndpointStatus('Accounts', 'Operational'),
      () => this.updateEndpointStatus('Accounts', 'Down')
    );
    this.apiService.checkAlgorithmsServiceHealth().subscribe(
      () => this.updateEndpointStatus('Algorithms', 'Operational'),
      () => this.updateEndpointStatus('Algorithms', 'Down')
    );
    this.apiService.checkAdminsServiceHealth().subscribe(
      () => this.updateEndpointStatus('Admins', 'Operational'),
      () => this.updateEndpointStatus('Admins', 'Down')
    );
    this.apiService.checkDatasetOpsServiceHealth().subscribe(
      () => this.updateEndpointStatus('DatasetOps', 'Operational'),
      () => this.updateEndpointStatus('DatasetOps', 'Down')
    );
    this.apiService.checkDatasetsServiceHealth().subscribe(
      () => this.updateEndpointStatus('Datasets', 'Operational'),
      () => this.updateEndpointStatus('Datasets', 'Down')
    );
    this.apiService.checkDoctorsServiceHealth().subscribe(
      () => this.updateEndpointStatus('Doctors', 'Operational'),
      () => this.updateEndpointStatus('Doctors', 'Down')
    );
    this.apiService.checkModelsServiceHealth().subscribe(
      () => this.updateEndpointStatus('Models', 'Operational'),
      () => this.updateEndpointStatus('Models', 'Down')
    );
    this.apiService.checkPatientsServiceHealth().subscribe(
      () => this.updateEndpointStatus('Patients', 'Operational'),
      () => this.updateEndpointStatus('Patients', 'Down')
    );
    this.apiService.checkWidgetsServiceHealth().subscribe(
      () => this.updateEndpointStatus('Widgets', 'Operational'),
      () => this.updateEndpointStatus('Widgets', 'Down')
    );
    this.apiService.checkUtilsServiceHealth().subscribe(
      () => this.updateEndpointStatus('Utils', 'Operational'),
      () => this.updateEndpointStatus('Utils', 'Down')
    );
  }

  updateEndpointStatus(name: string, status: string): void {
    const endpoint = this.endpoints.find(ep => ep.name === name);
    if (endpoint) {
      endpoint.status = status;
    }
  }

  selectEndpoint(endpoint: Endpoint): void {
    this.selectedEndpoint = endpoint;
  }
}
