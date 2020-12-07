import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable, of } from 'rxjs';

import { Record } from './record';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({ providedIn: 'root' })
export class RecordService {

  private apiUrl = 'http://localhost:5000/api/v1';  // URL to REST API

  constructor(private http: HttpClient) { }

  getRecords(): Observable<Record[]> {
    return this.http.get<Record[]>(this.apiUrl + '/records');
  }
  
  getRecord(id: number): Observable<any> {
    const url = `${this.apiUrl}/records/${id}`;
    return this.http.get<Record>(url);
  }
  
  addRecord(record: Record) {
	//console.log(record);
    return this.http.post(this.apiUrl, record, httpOptions);
  }
  
  updateRecord(record: Record): Observable<any> {
    const url = `${this.apiUrl}/records/${record.id}`;
    return this.http.put(url, record, httpOptions);
  }
  
  deleteRecord(record: Record | number) {
	  if (confirm("Are you sure to delete?")) {
		const id = typeof record === 'number' ? record : record.id;
		const url = `${this.apiUrl}/records/${id}`;
		return this.http.delete(url, httpOptions);
	  }
	  return of({});
  }
  
}