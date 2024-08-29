// doctor-book.component.ts
import { Component } from '@angular/core';
import { PatientModule } from '../../../Modules/patient/patient.module';

@Component({
  selector: 'app-doctor-book',
  templateUrl: './doctor-book.component.html',
  styleUrls: ['./doctor-book.component.css']
})
export class DoctorBookComponent {
  selectedPatient: PatientModule | null = null;

  constructor() {}

  onSelectPatient(patient: PatientModule) {
    this.selectedPatient = patient;
  }
}