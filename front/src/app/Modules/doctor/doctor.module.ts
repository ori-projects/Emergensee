import { Account } from "../account/accountModule";
import { PatientModule } from "../patient/patient.module";

export class DoctorModule extends Account {
  rank: string;
  phoneNumber: string;
  numberOfPatients: number;
  active: boolean;
  dateOfBirth: Date;
  patients: PatientModule[];

  constructor(name: string, id: number, rank: string, phoneNumber: string, numberOfPatients: number, active: boolean, imagePath: string, dateOfBirth: Date, email: string, password: string, role: string, isActive: boolean, patients: PatientModule[]) {
      super(   
        id,
        name,
        imagePath,
        email,
        password,
        role,
        isActive)
      this.rank = rank;
      this.phoneNumber = phoneNumber;
      this.numberOfPatients = numberOfPatients;
      this.active = active;
      this.dateOfBirth = dateOfBirth;
      this.patients = patients;
  }
}