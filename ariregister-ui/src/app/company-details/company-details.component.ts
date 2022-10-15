import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { faWarning, faUser, faBuilding } from '@fortawesome/free-solid-svg-icons';
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
  ownerRoleList: any;
  warningIcon = faWarning;
  privateIcon = faUser;
  businessIcon = faBuilding;

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
    this.Api.getList('ownerRole').subscribe((res: any) => {
      this.ownerRoleList = res;
    })
  }

  ngOnDestroy() {
    this.sub.unsubscribe();
  }

}
