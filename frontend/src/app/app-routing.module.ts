import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { RecordListComponent } from './record-list/record-list.component';
import { RecordAddComponent } from './record-add/record-add.component';
import { RecordEditComponent } from './record-edit/record-edit.component';
import { RecordDetailComponent } from './record-detail/record-detail.component';
import { StatisticsComponent } from './statistics/statistics.component';
import { HomeComponent } from './home/home.component';

const routes: Routes = [
  { path: '', component: HomeComponent, pathMatch: 'full' },
  { path: 'records', component: RecordListComponent },
  { path: 'records/:id/detail', component: RecordDetailComponent },
  { path: 'records/:id/edit', component: RecordEditComponent },
  { path: 'add', component: RecordAddComponent },
  { path: 'statistics', component: StatisticsComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
