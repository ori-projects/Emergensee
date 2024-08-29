import { Component, Output, EventEmitter, OnInit } from '@angular/core';
import { PatientModule } from '../../../Modules/patient/patient.module';
import { ApiService } from '../../../Services/api.service';
import { PatientMapper } from '../../../Mappers/patient.mapper'; 
import { AuthService } from '../../../Services/auth.service';

@Component({
  selector: 'app-patient-list',
  templateUrl: './patient-list.component.html',
  styleUrls: ['./patient-list.component.css'],
})
export class PatientListComponent implements OnInit {
  @Output() selectPatient: EventEmitter<PatientModule> = new EventEmitter<PatientModule>();
  patients: PatientModule[] = [];
  selectedPatient: PatientModule | null = null;
  isNewPatient = false;
  filterText: string = '';
  filteredPatients: PatientModule[] = [];

  constructor(private apiService: ApiService, private authService: AuthService) {}

  ngOnInit() {
    this.getPatientsByDoctorId(this.authService.getId()); // Replace with actual doctor ID
  }

  onSelectPatient(patient: PatientModule) {
    this.selectedPatient = patient;
    this.selectPatient.emit(patient);
  }

  CreateNewPatient() {
    var patient = new PatientModule('', '', null, '', '', '', '', '', '', '', '', '', '', '', '', '','');
    this.selectedPatient = patient;
    this.isNewPatient = true;
    this.selectPatient.emit(patient);
  }

  filterPatients() {
    this.filteredPatients = this.patients.filter((patient) =>
      patient.name.toLowerCase().includes(this.filterText.toLowerCase())
    );
  }

  private getPatientsByDoctorId(doctorId: number): void {
    this.apiService.getPatientsByDoctorId(doctorId).subscribe(
      (patients: any[]) => {
        this.patients = patients.map(patientData => PatientMapper.mapToPatient(patientData));
        this.filteredPatients = [...this.patients];
      },
      error => {
        console.error('Error fetching patients:', error);
      }
    );
  }

  onPatientSaved() {
    this.getPatientsByDoctorId(this.authService.getId());
  }
}
