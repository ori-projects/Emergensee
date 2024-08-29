import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, map } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class GoogleDriveService {

  constructor(private http: HttpClient) {}

  uploadImageToDrive(imageData: Blob, fileName: string, accessToken: string): Observable<any> {
    const formData = new FormData();
    formData.append('file', imageData, fileName);

    return this.http.post<any>('https://www.googleapis.com/upload/drive/v3/files?uploadType=media', formData, {
      headers: {
        Authorization: `Bearer ${accessToken}`,
        'Content-Type': 'image/jpeg' // Adjust content type accordingly
      }
    });
  }

  getFileMetadata(fileId: string, accessToken: string): Observable<any> {
    return this.http.get<any>(`https://www.googleapis.com/drive/v3/files/${fileId}`, {
      headers: {
        Authorization: `Bearer ${accessToken}`
      }
    });
  }

  getPublicLink(fileId: string, accessToken: string): Observable<string> {
    return this.getFileMetadata(fileId, accessToken).pipe(
      map((metadata: any) => metadata.webViewLink)
    );
  }
}