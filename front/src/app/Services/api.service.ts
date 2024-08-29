import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError, map } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private AccountsServiceUrl = 'http://127.0.0.1:8001';
  private AdminsServiceUrl = 'http://127.0.0.1:8002';
  private AlgorithmsServiceUrl = 'http://127.0.0.1:8003';
  private DatasetOpsServiceUrl = 'http://127.0.0.1:8004';
  private DatasetsServiceUrl = 'http://127.0.0.1:8005';
  private DoctorsServiceUrl = 'http://127.0.0.1:8006';
  private ModelsServiceUrl = 'http://127.0.0.1:8007';
  private PatientsServiceUrl = 'http://127.0.0.1:8008';
  private WidgetsServiceUrl = 'http://127.0.0.1:8009';
  private UtilsServiceUrl = 'http://127.0.0.1:8010';
  private ToolsServiceUrl = 'http://127.0.0.1:8011';

  constructor(private http: HttpClient) { }
    //Get risk assesment doctor
    getRiskAssessment(formData: any): Observable<any> {
      return this.http.post<any>(`${this.DatasetOpsServiceUrl}/get-risk-assessment`, formData);
    }

    getEnums(): Observable<any> {
      return this.http.get<any>(`${this.UtilsServiceUrl}/get-enums`);
    }

    // Create patient 
    createPatient(formData: any): Observable<any> {
      console.log(formData);
      return this.http.post<any>(`${this.PatientsServiceUrl}/create-patient`, formData)
        .pipe(
          map(response => {
            return response;
          }),
          catchError(error => {
            throw error;
          })
        );
      }

    createAccount(formData: any): Observable<any> {
      return this.http.post<any>(`${this.AccountsServiceUrl}/create-account`, formData)
        .pipe(
          map(response => {
            return response;
          }),
          catchError(error => {
            throw error;
          })
        );
      }


      deleteAccount(formData: any): Observable<any> {
        return this.http.post<any>(`${this.AccountsServiceUrl}/delete-account`, formData)
          .pipe(
            map(response => {
              return response;
            }),
            catchError(error => {
              throw error;
            })
          );
        }


    //get patients
    getPatientsByDoctorId(accountId: number): Observable<any> {
      return this.http.get<any>(`${this.PatientsServiceUrl}/get-patients/${accountId}`);
    }

    //deletePatientsById(accountId: number): Observable<any> {
    //  return this.http.get<any>(`${this.PatientsServiceUrl}/get-patients/${accountId}`);
    //}

    //Login

    login(formData: any): Observable<any> {
      return this.http.post<any>(`${this.AccountsServiceUrl}/login`, formData)
        .pipe(
          map(response => {
            return response;
          }),
          catchError(error => {
            throw error;
          })
        );
      }
  

    // Get datasets 
    getDatasets(): Observable<any> {
      return this.http.get<any>(`${this.DatasetsServiceUrl}/get-datasets`);
    }

    // Health check methods
    checkAccountsServiceHealth(): Observable<any> {
      return this.http.get<any>(`${this.AccountsServiceUrl}/health`);
    }

    checkAlgorithmsServiceHealth(): Observable<any> {
      return this.http.get<any>(`${this.AlgorithmsServiceUrl}/health`);
    }
    
    checkAdminsServiceHealth(): Observable<any> {
      return this.http.get<any>(`${this.AdminsServiceUrl}/health`);
    }
  
    checkDatasetOpsServiceHealth(): Observable<any> {
      return this.http.get<any>(`${this.DatasetOpsServiceUrl}/health`);
    }
  
    checkDatasetsServiceHealth(): Observable<any> {
      return this.http.get<any>(`${this.DatasetsServiceUrl}/health`);
    }
  
    checkDoctorsServiceHealth(): Observable<any> {
      return this.http.get<any>(`${this.DoctorsServiceUrl}/health`);
    }
  
    checkModelsServiceHealth(): Observable<any> {
      return this.http.get<any>(`${this.ModelsServiceUrl}/health`);
    }
  
    checkPatientsServiceHealth(): Observable<any> {
      return this.http.get<any>(`${this.PatientsServiceUrl}/health`);
    }
  
    checkWidgetsServiceHealth(): Observable<any> {
      return this.http.get<any>(`${this.WidgetsServiceUrl}/health`);
    }
  
    checkUtilsServiceHealth(): Observable<any> {
      return this.http.get<any>(`${this.UtilsServiceUrl}/health`);
    }
  
    checkToolsServiceHealth(): Observable<any> {
      return this.http.get<any>(`${this.ToolsServiceUrl}/health`);
    }

    // Get accounts 
    getAccounts(id: number): Observable<any> {
      const requestData = { id: id };
      return this.http.post<any>(`${this.AccountsServiceUrl}/get-accounts`, requestData);
    }
}