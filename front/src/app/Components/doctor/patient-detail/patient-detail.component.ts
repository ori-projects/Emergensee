import { Component, Input, Output, EventEmitter } from '@angular/core';
import { PatientModule } from '../../../Modules/patient/patient.module';
import { ApiService } from '../../../Services/api.service';
import { MatDialog } from '@angular/material/dialog';
import { ResponseModalComponent } from '../../shared/response-modal/response-modal.component';
import { RankingModalComponent } from '../../shared/ranking-system/ranking-system.component';
import { AuthService } from '../../../Services/auth.service';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-patient-detail',
  templateUrl: './patient-detail.component.html',
  styleUrls: ['./patient-detail.component.css'],
})
export class PatientDetailComponent {
  private _selectedPatient: PatientModule | null = null;
  @Input() set selectedPatient(value: PatientModule | null) {
    this._selectedPatient = value;
    if (value) {
      this.resetFormState(null);
    }
  }
  @Output() patientSaved: EventEmitter<PatientModule> = new EventEmitter<PatientModule>();
  get selectedPatient(): PatientModule | null {
    return this._selectedPatient;
  }

  isNewPatient = false; // Flag to check if it's a new patient
  waiting: boolean = false;
  showDetails = false; // Controls the visibility of the form section
  showButton = true; // Controls the visibility of the button
  imageFile: File | null = null; // For storing the image file
  imagePreviewUrl: string | ArrayBuffer | null = null;

  operativeProcedureOptions: string[] = [];
  feelingsAndUrgeOptions: string[] = [];
  diseaseOptions: string[] = [];
  criticalFeelingsOptions: string[] = [];

  diseaseRating: number = null;
  ckdRating: number = null;
  sirRating: number = null;
  maRating: number = null;

  constructor(private apiService: ApiService, public dialog: MatDialog, private authService: AuthService, private http: HttpClient) {
    this.apiService.getEnums().subscribe((response) => {
      this.operativeProcedureOptions = response.enums.Operative_Procedure;
      this.feelingsAndUrgeOptions = response.enums.Feelings_and_Urge;
      this.diseaseOptions = response.enums.Disease;
      this.criticalFeelingsOptions = response.enums.Critical_Feelings;
    });
  }

  ngOnChanges(): void {
    this.isNewPatient = !this.selectedPatient?.name;
  }

  resetFormState(patient: PatientModule | null): void {
    this.isNewPatient = !this.selectedPatient?.name;
    this.showDetails = false;
    this.showButton = true;
  }

  toggleDetails(): void {
    this.showDetails = !this.showDetails;
  }

  handleFileInput(event: any) {
    const file = event.target.files[0];
    if (file) {
      if (!file.type.startsWith('image/')) {
        console.error('Unsupported file type');
        return;
      }
      this.imageFile = file;
      this.previewImage(); // Implement this if needed
    }
  }
  
  previewImage() {
    if (!this.imageFile) return;

    const reader = new FileReader();
    reader.readAsDataURL(this.imageFile);
    reader.onload = () => {
      this.imagePreviewUrl = reader.result;
    };
  }

  saveNewPatient() {
    if (this.selectedPatient && this.imageFile) {
      const reader = new FileReader();
  
      reader.onloadend = () => {
        // 'result' contains the base64 representation of the file
        const base64String = reader.result as string;
        this.selectedPatient.image = base64String; // Assign base64 string to patient object
  
        const formDataObject = {
          name: this.selectedPatient.name,
          age: this.selectedPatient.age,
          email: this.selectedPatient.email,
          doctor_id: this.authService.getId().toString(),
          image: this.selectedPatient.image, // Include base64 image string in form data
          phone_number: this.selectedPatient.phoneNumber
        };
  
        this.apiService.createPatient(formDataObject).subscribe(
          (response) => {
            this.isNewPatient = false;
            this.patientSaved.emit(this.selectedPatient);
            //HERE REBUILD THE APP
          },
          (error) => {
            console.error('Error creating patient:', error);
          }
        );
      };
  
      reader.readAsDataURL(this.imageFile);
    }
  }  

  submitForm() {
    if (this.diseaseRating === null || this.ckdRating === null || this.sirRating === null || this.maRating === null) {
      return;
    }

    const formData = {
      name: this.selectedPatient?.name,
      email: this.selectedPatient?.email,
      phoneNumber: this.selectedPatient?.phoneNumber,
      age: this.selectedPatient?.age.toString(),
      bloodPressure: this.selectedPatient?.bloodPressure,
      bloodSugar: this.selectedPatient?.bloodSugar,
      procedureCount: this.selectedPatient?.procedureCount,
      infectionsReported: this.selectedPatient?.infectionsReported,
      bodyTemperature: this.selectedPatient?.bodyTemperature,
      heartRate: this.selectedPatient?.heartRate,
      operativeProcedure: this.selectedPatient?.operativeProcedure,
      feelingsAndUrge: this.selectedPatient?.feelingsAndUrge,
      criticalFeelings: this.selectedPatient?.criticalFeelings,
      disease: this.selectedPatient?.disease,
      diseaseRating: this.diseaseRating,
      ckdRating: this.ckdRating,
      sirRating: this.sirRating,
      maRating: this.maRating,
    };

    this.waiting = true;

    this.apiService.getRiskAssessment(formData).subscribe(
      response => {
        this.waiting = false;
        this.openResponseModal(response.message);
      },
      error => {
        this.waiting = false;
        console.error(error);
        this.openResponseModal('An error occurred while processing your request.');
      }
    );
  }

  openRankingModal(): void {
    const dialogRef = this.dialog.open(RankingModalComponent, {
      width: '400px'
    });

    dialogRef.afterClosed().subscribe(result => {
      if (result) {
        this.diseaseRating = result.diseaseRating;
        this.ckdRating = result.ckdRating;
        this.sirRating = result.sirRating;
        this.maRating = result.maRating;
      }
      this.showDetails = true;
      this.showButton = false;
    });
  }

  openResponseModal(message: string): void {
    const formattedMessage = this.formatMessage(message);
    const dialogRef = this.dialog.open(ResponseModalComponent, {
      width: '400px',
      data: formattedMessage
    });
  
    dialogRef.afterClosed().subscribe(() => {});
  }
  
  private formatMessage(message: string): { finalAssessment: string; components: string[] } {
    const lines = message.split('\n').map(line => line.trim());
    const finalAssessmentLine = lines[0].replace('- ', '');
    const components = lines.slice(1).map(line => line);
    return {
      finalAssessment: finalAssessmentLine,
      components
    };
  }
}
