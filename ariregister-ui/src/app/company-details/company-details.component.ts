import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AriregisterApiService } from '../services/ariregister-api.service'; 

@Component({
  selector: 'app-company-details',
  templateUrl: './company-details.component.html',
  styleUrls: ['./company-details.component.css']
})
export class CompanyDetailsComponent implements OnInit, OnDestroy {
  id: number = 0;
  private sub: any;
  companyData: any;
  companyOwners: any;

  constructor(private route: ActivatedRoute,
    private Api: AriregisterApiService) { }

  ngOnInit() {
    this.sub = this.route.params.subscribe(params => {
      this.id = +params['id']; 
    });

    this.Api.getCompanyData(this.id).subscribe((res: any) => {
      this.companyData = res;
    });

    this.Api.getCompanyOwners(this.id).subscribe((res: any) => {
      this.companyOwners = res;
    })
  }

  ngOnDestroy() {
    this.sub.unsubscribe();
  }

}
