import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable, of } from 'rxjs';

import { Statistics } from './statistics';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({ providedIn: 'root' })
export class StatisticsService {

  private apiUrl = 'http://localhost:5000/api/v1';  // URL to REST API

  constructor(private http: HttpClient) { }

  getStatistics() {
    return this.http.get<Statistics>(this.apiUrl + '/statistics');
  }
  
}