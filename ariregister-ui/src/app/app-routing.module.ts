import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CompanySearchComponent } from './company-search/company-search.component';
import { CompanyAddComponent } from './company-add/company-add.component';
import { CompanyDetailsComponent } from './company-details/company-details.component';
import { Err404Component } from './err404/err404.component';

const routes: Routes = [
  {path: '', component: CompanySearchComponent},
  {path: 'add-company', component: CompanyAddComponent},
  {path: 'company-details/:id', component: CompanyDetailsComponent},
  {path: '**', component: Err404Component},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponents = [CompanySearchComponent, CompanyAddComponent, CompanyDetailsComponent, Err404Component]