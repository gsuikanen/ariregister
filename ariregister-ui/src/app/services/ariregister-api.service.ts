import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { retry } from 'rxjs';
import { ApiEndpoints } from '../api/ariregister-api';

@Injectable({
  providedIn: 'root'
})
export class AriregisterApiService {

  constructor(private http: HttpClient) {
  }

  getList(listName: string) {
    return this.http.get<any>(ApiEndpoints.BASE_URL + ApiEndpoints.GET_LIST + '/' + listName)
    .pipe(retry({count: 3, delay: 500}))
  }

  getCompanyHints(searchString: string) {
    let params = new HttpParams().set('searchstring', searchString);
    return this.http.get<any>(ApiEndpoints.BASE_URL + ApiEndpoints.GET_COMPANIES_BY_SEARCHSTRING, {params})
    .pipe(retry({count: 3, delay: 500}))
  }

  getCompanyData(id: number) {
    let params = new HttpParams().set('id', id);
    return this.http.get<any>(ApiEndpoints.BASE_URL + ApiEndpoints.GET_COMPANY_BY_ID, {params})
    .pipe(retry({count: 3, delay: 500}))
  }

  getCompanyOwners(id: number) {
    let params = new HttpParams().set('id', id);
    return this.http.get<any>(ApiEndpoints.BASE_URL + ApiEndpoints.GET_COMPANY_OWNERS, {params})
    .pipe(retry({count: 3, delay: 500}))
  }

  postCompanyData(data: any) {
    var body = JSON.stringify(data);
    var headers = new HttpHeaders({'Content-type': 'application/json', 'Data-type': 'json'})
    return this.http.post<any>(ApiEndpoints.BASE_URL + ApiEndpoints.POST_COMPANY_DATA, body, {headers: headers})
  }
}

