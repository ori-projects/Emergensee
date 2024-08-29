import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { NgChartsModule } from 'ng2-charts';
import { RouterModule, Routes } from '@angular/router';
import { ReactiveFormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { PatientEditComponent } from './Components/doctor/patient-edit/patient-edit.component';
import { PatientDetailComponent } from './Components/doctor/patient-detail/patient-detail.component';
import { DoctorBookComponent } from './Components/doctor/doctor-book/doctor-book.component';
import { PatientListComponent } from './Components/doctor/patient-list/patient-list.component';
import { MlmodelDetailComponent } from './Components/admin/dataset/mlmodel-detail/mlmodel-detail.component';
import { DecisiondatasetListComponent } from './Components/admin/dataset/decision-dataset-list/decision-dataset-list.component';
import { HeaderComponent } from './Components/header/header.component';
import { LoginComponent } from './Components/login/login.component';
import { datasetComponent } from './Components/admin/dataset/dataset/dataset.component';
import { DashboardComponent } from './Components/admin/dashboard/dashboard.component';
import { DecisiondatasetDetailComponent } from './Components/admin/dataset/decision-dataset-detail/decision-dataset-detail.component';
import { HttpClientModule } from '@angular/common/http';
import { AccountListComponent } from './Components/admin/account-list/account-list.component';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { MatDialogModule } from '@angular/material/dialog';
import { ResponseModalComponent } from './Components/shared/response-modal/response-modal.component';
import { RankingModalComponent } from './Components/shared/ranking-system/ranking-system.component';


const appRoutes: Routes = [
  { path: '', redirectTo: '/login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'patients', component: DoctorBookComponent },
  { path: 'dashboard', component: DashboardComponent },
  { path: 'dataset', component: datasetComponent },
  { path: 'accounts', component: AccountListComponent },
];

@NgModule({
  declarations: [
    AppComponent,
    PatientEditComponent,
    PatientDetailComponent,
    DoctorBookComponent,
    PatientListComponent,
    MlmodelDetailComponent,
    DecisiondatasetListComponent,
    DecisiondatasetDetailComponent,
    HeaderComponent,
    LoginComponent,
    datasetComponent,
    DashboardComponent,
    AccountListComponent,
    ResponseModalComponent,
    RankingModalComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    ReactiveFormsModule,
    NgChartsModule,
    HttpClientModule,
    MatDialogModule,
    RouterModule.forRoot(appRoutes),
  ],
  providers: [
    provideAnimationsAsync()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
