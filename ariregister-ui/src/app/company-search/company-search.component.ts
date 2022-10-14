import { Component, OnInit } from '@angular/core';
import { faSearch, faWarning, faChevronRight } from '@fortawesome/free-solid-svg-icons';
import { AriregisterApiService } from '../services/ariregister-api.service'; 

@Component({
  selector: 'app-company-search',
  templateUrl: './company-search.component.html',
  styleUrls: ['./company-search.component.css']
})
export class CompanySearchComponent implements OnInit {
  searchIcon = faSearch;
  warningIcon = faWarning;
  arrowIcon = faChevronRight;
  p = 1

  companies: any;

  constructor(private Api: AriregisterApiService) {
   }

  ngOnInit(): void {
  }

  getCompanyHints(searchString: string) { 
    this.Api.getCompanyHints(searchString).subscribe((res: any) => {
      this.companies = res;
    })
  }
  
  enterPressed(event?: Event) {
    const target = event?.target as HTMLInputElement;
    this.getCompanyHints(target.value);
  }

}
